import os
import args_manager
import modules.config
import json
import urllib.parse

from PIL import Image
from PIL.PngImagePlugin import PngInfo
from modules.util import generate_temp_filename
from tempfile import gettempdir

log_cache = {}


def get_current_html_path(image_extension=None):
    _image_extension = image_extension if image_extension else modules.config.default_image_extension
    date_string, local_temp_filename, only_name = generate_temp_filename(folder=modules.config.path_outputs,
                                                                         extension=_image_extension)
    html_name = os.path.join(os.path.dirname(local_temp_filename), 'log.html')
    return html_name


def log(img, dic, metadata=None, save_metadata_to_image=False, image_file_extension=None) -> str:
    path_outputs = args_manager.args.temp_path if args_manager.args.disable_image_log else modules.config.path_outputs
    image_file_extension = image_file_extension if image_file_extension else modules.config.default_image_file_extension
    date_string, local_temp_filename, only_name = generate_temp_filename(folder=path_outputs, extension=image_file_extension)
    os.makedirs(os.path.dirname(local_temp_filename), exist_ok=True)

    if image_file_extension == 'png':
        if save_metadata_to_image:
            pnginfo = PngInfo()
            pnginfo.add_text("parameters", metadata)
        else:
            pnginfo = None
        Image.fromarray(img).save(local_temp_filename, pnginfo=pnginfo)
    elif image_file_extension == 'jpg':
        # TODO check if metadata works correctly here
        Image.fromarray(img).save(local_temp_filename, quality=95, optimize=True, progressive=True, comment=metadata if save_metadata_to_image else None)
    elif image_file_extension == 'webp':
        # TODO test exif handling
        Image.fromarray(img).save(local_temp_filename, quality=95, lossless=False)
    else:
        Image.fromarray(img).save(local_temp_filename)

    if args_manager.args.disable_image_log:
        return local_temp_filename

    html_name = os.path.join(os.path.dirname(local_temp_filename), 'log.html')

    css_styles = (
        "<style>"
        "body { background-color: #121212; color: #E0E0E0; } "
        "a { color: #BB86FC; } "
        ".metadata { border-collapse: collapse; width: 100%; } "
        ".metadata .key { width: 15%; } "
        ".metadata .value { width: 85%; font-weight: bold; } "
        ".metadata th, .metadata td { border: 1px solid #4d4d4d; padding: 4px; } "
        ".image-container img { height: auto; max-width: 512px; display: block; padding-right:10px; } "
        ".image-container div { text-align: center; padding: 4px; } "
        "hr { border-color: gray; } "
        "button { background-color: black; color: white; border: 1px solid grey; border-radius: 5px; padding: 5px 10px; text-align: center; display: inline-block; font-size: 16px; cursor: pointer; }"
        "button:hover {background-color: grey; color: black;}"
        "</style>"
    )

    js = (
        """<script>
        function to_clipboard(txt) { 
        txt = decodeURIComponent(txt);
        if (navigator.clipboard && navigator.permissions) {
            navigator.clipboard.writeText(txt)
        } else {
            const textArea = document.createElement('textArea')
            textArea.value = txt
            textArea.style.width = 0
            textArea.style.position = 'fixed'
            textArea.style.left = '-999px'
            textArea.style.top = '10px'
            textArea.setAttribute('readonly', 'readonly')
            document.body.appendChild(textArea)

            textArea.select()
            document.execCommand('copy')
            document.body.removeChild(textArea)
        }
        alert('Copied to Clipboard!\\nPaste to prompt area to load parameters.\\nCurrent clipboard content is:\\n\\n' + txt);
        }
        </script>"""
    )

    begin_part = f"<html><head><title>Fooocus Log {date_string}</title>{css_styles}</head><body>{js}<p>Fooocus Log {date_string} (private)</p>\n<p>All images are clean, without any hidden data/meta, and safe to share with others.</p><!--fooocus-log-split-->\n\n"
    end_part = f'\n<!--fooocus-log-split--></body></html>'

    middle_part = log_cache.get(html_name, "")

    if middle_part == "":
        if os.path.exists(html_name):
            existing_split = open(html_name, 'r', encoding='utf-8').read().split('<!--fooocus-log-split-->')
            if len(existing_split) == 3:
                middle_part = existing_split[1]
            else:
                middle_part = existing_split[0]

    div_name = only_name.replace('.', '_')
    item = f"<div id=\"{div_name}\" class=\"image-container\"><hr><table><tr>\n"
    item += f"<td><a href=\"{only_name}\" target=\"_blank\"><img src='{only_name}' onerror=\"this.closest('.image-container').style.display='none';\" loading='lazy'></img></a><div>{only_name}</div></td>"
    item += "<td><table class='metadata'>"
    for key, value in dic:
        value_txt = str(value).replace('\n', ' </br> ')
        item += f"<tr><td class='key'>{key}</td><td class='value'>{value_txt}</td></tr>\n"
    item += "</table>"

    js_txt = urllib.parse.quote(json.dumps({k: v for k, v in dic}, indent=0), safe='')
    item += f"</br><button onclick=\"to_clipboard('{js_txt}')\">Copy to Clipboard</button>"

    item += "</td>"
    item += "</tr></table></div>\n\n"

    middle_part = item + middle_part

    with open(html_name, 'w', encoding='utf-8') as f:
        f.write(begin_part + middle_part + end_part)

    print(f'Image generated with private log at: {html_name}')

    log_cache[html_name] = middle_part

    return local_temp_filename
