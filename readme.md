# Fooocus - mashb1t's 1-Up Edition

The purpose of this fork is to add new features / fix bugs and contribute back to [Fooocus](https://github.com/lllyasviel/Fooocus).

As a collaborator & contributor of the Fooocus repository you can find me in almost every [issue](https://github.com/lllyasviel/Fooocus/issues), [pull request](https://github.com/lllyasviel/Fooocus/pulls), [discussion](https://github.com/lllyasviel/Fooocus/discussions) etc.

Sadly the creator of Fooocus has gone dark multiple times for an extended amount of time, which is why I took matters into my own hands.

![BillsUghGIF](https://github.com/mashb1t/Fooocus/assets/9307310/78c04e06-8ef0-4224-9c25-8f1bee9861de)

## Additional features included in this fork:
(mostly a reflection of [my PRs](https://github.com/lllyasviel/Fooocus/pulls/mashb1t))

* ✨ https://github.com/lllyasviel/Fooocus/pull/958 - NSFW image censoring (config and UI)
* 🐛 https://github.com/lllyasviel/Fooocus/pull/981 - prevent users from skipping/stopping other users tasks in queue (multi-user capabilities) + rework advanced_parameters (removal + PID handling)
* ✨ https://github.com/lllyasviel/Fooocus/pull/985 - add list of 100 animals to wildcards
* ✨ https://github.com/lllyasviel/Fooocus/pull/1013 - add advanced parameter for disable_intermediate_results (progress_gallery, prevents UI lag when generation is too fast)
* ✨ https://github.com/lllyasviel/Fooocus/pull/1039 - add prompt translation
* ✨ https://github.com/lllyasviel/Fooocus/pull/1043 - add lcm realtime canvas painting (not merged to main in this repository)
* ✨ ~~https://github.com/lllyasviel/Fooocus/pull/1167 - update model BluePencil XL v0.5 to v3.1.0~~
* ✨ https://github.com/lllyasviel/Fooocus/pull/1570 - add preset selection to Gradio UI (session based)
* 🐛 ~~https://github.com/lllyasviel/Fooocus/pull/1578 - add workaround for changing prompt while generating~~
* ✨ https://github.com/lllyasviel/Fooocus/pull/1580 - add preset for SDXL Turbo (model DreamShaperXL_Turbo)
* ✨ ~~https://github.com/lllyasviel/Fooocus/pull/1616 - add config setting for default_max_image_number~~
* 🐛 https://github.com/lllyasviel/Fooocus/pull/1668 - fix path_outputs directory creation if it doesn't exist
* ✨ show more details for each performance setting, e.g. steps
* ✨ add default_overwrite_step handling for meta data and gradio (allows turbo preset switching to set default_overwrite_step correctly)
* ✨ ~~https://github.com/lllyasviel/Fooocus/pull/1762 - add style preview on mouseover~~
* 🐛 ~~https://github.com/lllyasviel/Fooocus/pull/1784 - correctly sort files, display deepest directory level first~~
* ✨ ~~https://github.com/lllyasviel/Fooocus/pull/1785 - update model Juggernaut XL v6 to v8~~
* ✨ https://github.com/lllyasviel/Fooocus/pull/1809 - reduce file size of preview images
* ✨ https://github.com/lllyasviel/Fooocus/pull/1932 - use consistent file name in gradio
* ✨ https://github.com/lllyasviel/Fooocus/pull/1863 - image extension support (png, jpg, webp)
* ✨ https://github.com/lllyasviel/Fooocus/pull/1938 - automatically describe image on uov image upload if prompt is empty
* ✨ https://github.com/lllyasviel/Fooocus/pull/1940 - meta data handling, schemes: Fooocus (json) and A1111 (plain text). Compatible with Civitai.
* ✨ ~~https://github.com/lllyasviel/Fooocus/pull/1979 - prevent outdated history log link after midnight~~
* ✨ https://github.com/lllyasviel/Fooocus/pull/2032 - add inpaint mask generation functionality using rembg, incl. segmentation support

✨ = new feature<br>
🐛 = bugfix<br>
~~abc~~ = merged

---

## Feature showcase

### https://github.com/lllyasviel/Fooocus/pull/1570 - Preset Selection

No need to restart your browser to change a preset ever again. Combined with total user isolation, every user can now set and use any preset they desire.
You can even reload your presets in the browser if you've changed them.

![image](https://github.com/mashb1t/Fooocus/assets/9307310/9b302b04-bbbc-4a21-9ccf-02d2b534d481)

---

### https://github.com/lllyasviel/Fooocus/pull/2032 - Automated Mask Generation + Mask Prompting

https://github.com/mashb1t/Fooocus/assets/9307310/b69bf607-128b-48a6-a248-fa2b09218fe7

Videos by [@rayronvictor](https://github.com/rayronvictor)

<details><summary>Mask generation by cloth category</summary>
<p>

https://github.com/mashb1t/Fooocus/assets/9307310/204a01f6-63af-4fd2-bd92-76e176849f19

</p>
</details> 

<details><summary>Mask generation by prompt</summary>
<p>

https://github.com/mashb1t/Fooocus/assets/9307310/b69bf607-128b-48a6-a248-fa2b09218fe7

</p>
</details> 

---

### https://github.com/lllyasviel/Fooocus/pull/1940 - Metadata Handling - Compatible with Civitai & A1111
This feature offers activatable metadata persistency in images for both a Fooocus (json) and A1111 (plain text) meta data scheme, where the latter is 100% compatible with A1111 and Civitai, but can not be used to reproduce the image outside of Fooocus, as there are so many improvements and special things happening in Fooocus it's just not applicable anywhere else.
- Supports metadata for PNG (PngInfo) + JPG and WebP (both EXIF).
- Save & restore configurations directly from images
- You can also configure a copyright / creator tag

![Screenshot 2024-01-29 at 15 13 17](https://github.com/lllyasviel/Fooocus/assets/9307310/6b7df4eb-feb3-46ee-bf09-f336be63b625)

<details><summary>Gradio (setting in Developer Debug Mode)</summary>
<p>

Default is Fooocus Scheme
![image](https://github.com/lllyasviel/Fooocus/assets/9307310/ae529db2-f5d1-4725-9735-3036b50020b7)

</p>
</details> 

<details><summary>Config options</summary>
<p>

    "default_save_metadata_to_images": true,
    "default_metadata_scheme": "a1111",
    "metadata_created_by": "mashb1t"

</p>
</details> 

<details><summary>Arg --disable-metadata</summary>
<p>

 `--disable-metadata` completely prevents metadata processing and output in Gradio

</p>
</details> 


<details><summary>Metadata Reader</summary>
<p>

1. open Image Input > Metadata tab
2. drag & Drop image to image upload
3. automatic preview of image metadata
4. apply metadata to Gradio inputs on button click

Fooocus scheme
![Screenshot 2024-01-29 at 15 13 17](https://github.com/lllyasviel/Fooocus/assets/9307310/6b7df4eb-feb3-46ee-bf09-f336be63b625)

A1111 scheme
![Screenshot 2024-01-29 at 15 09 52](https://github.com/lllyasviel/Fooocus/assets/9307310/1ee3c030-2b6d-41cb-9f88-40df6452df15)

</p>
</details> 


<details><summary>Metadata in files</summary>
<p>

Speed Fooocus scheme
![image](https://github.com/lllyasviel/Fooocus/assets/9307310/c556b2ed-0e0b-4117-9bda-9508fb3e0d96)

LCM A1111 scheme (yes, with negative prompt, because it technically exists but doesn't have an influence)
![image](https://github.com/lllyasviel/Fooocus/assets/9307310/322de4e1-00d7-428a-84db-64e4a9a5637e)

Speed A1111 scheme
![image](https://github.com/lllyasviel/Fooocus/assets/9307310/3b49627a-4e3f-4d13-b795-04db2743baab)

</p>
</details> 

<details><summary>Civitai</summary>
<p>

Speed Fooocus scheme
![image](https://github.com/lllyasviel/Fooocus/assets/9307310/1d31af41-d5a7-4f86-b89c-3aeeb1733417)

LCM A1111 scheme
![image](https://github.com/lllyasviel/Fooocus/assets/9307310/d91a4b71-ffe1-430b-8db0-0a5b0662d48f)

![image](https://github.com/lllyasviel/Fooocus/assets/9307310/e0e93b0e-30ee-4263-95de-05d56ff7a885)

Speed A1111 scheme
![image](https://github.com/lllyasviel/Fooocus/assets/9307310/1cf4b6d6-775d-4d68-99f2-a7dea34241b3)

![image](https://github.com/lllyasviel/Fooocus/assets/9307310/d55c6b6c-08e1-4fcb-a22e-39d45be1c0c2)


</p>
</details>

---

<div align=center>
<img src="https://github.com/lllyasviel/Fooocus/assets/19834515/483fb86d-c9a2-4c20-997c-46dafc124f25">

This is a fork of [Fooocus](https://github.com/lllyasviel/Fooocus).  This fork integrates the following:

* Insightface/[inswapper](https://github.com/haofanwang/inswapper) library used by roop, ReActor, and others
* [PhotoMaker](https://github.com/TencentARC/PhotoMaker) based on `🤗 diffusers`
* [InstantID](https://github.com/InstantID/InstantID) based on `🤗 diffusers`

The goal of this repository is to stay up-to-date with the main repository, while also maintaining the above integrations.

For more detailed and official documentation, please refer to [lllyasviel's repository](https://github.com/lllyasviel/Fooocus).

A standalone installation does not exist for this repository.

## Installation (Windows)

The installation assumes CUDA 11.8.  If you need a different version, please update `configure.bat` with the correct URL to the desired CUDA version.

1. Run `git clone https://github.com/machineminded/Fooocus-inswapper.git`
2. Execute `configure.bat`

## Inswapper Usage

Inswapper will activate if "Input Image" and "Enabled" are both checked.

1. `.\venv\Scripts\activate`
2. `python launch.py`

https://github.com/machineminded/Fooocus-inswapper/assets/155763297/68f69e95-8306-4c7b-8f9b-0013352460b6

## PhotoMaker Usage

In this fork, PhotoMaker utilizes `🤗 diffusers`, so it runs outside of the ksampler pipelines.  I'd like to eventually add inpainting and ControlNet for `🤗 diffusers` but it will take some time.  [Keep in mind that PhotoMaker currently requires 15GB of VRAM!](https://github.com/TencentARC/PhotoMaker?tab=readme-ov-file#-new-featuresupdates) The following Fooocus configuration items are passed to the PhotoMaker `🤗 diffusers` pipeline:

* Resolution (width and height)
* Prompt (and generated prompts from selected styles)
* Negative Prompt (and generated prompts from selected styles)
* Steps
* CFG/Guidance Scale
* Seed
* LoRAs
* Sampler (not fully implemented)
* Scheduler (not fully implemented)

### PhotoMaker General Usage

1. Navigate to the PhotoMaker tab.
2. Click "Enable"
3. Load images from your PC.
4. Enter your prompt and be sure to include "man img" or "woman img" depending on the subject at hand.  **img** in the prompt is expected by PhotoMaker.
5. Click "Generate"

Experiment with also adding an image to the Inswapper tab to overlay the generated image.

**Note: Unchecking "Enable" will unload the PhotoMaker pipeline from memory!**

### PhotoMaker LoRA Usage

1. Select the LoRAs you want to use as usual.
2. Navigate to the PhotoMaker tab.
3. Click "Enable" then click "Generate"

If you change the LoRAs or their weights:

1. Uncheck "Enabled" to unload the model from memory
2. Re-check "Enabled" and click "Generate" to reload the LoRAs and the pipeline into memory.

### Supported PhotoMaker samplers
* euler
* euler ancestral
* DPM++ 2M SDE
* DPM++ 2M SDE Karras
* Will default to DDIM Scheduler for anything else

## InstantID Usage

**[>>> Click here to download <<<](https://github.com/mashb1t/Fooocus/releases/download/2.1.864/Fooocus_mashb1t_win64_2-1-864.7z)**

In this fork, InstantID utilizes `🤗 diffusers`, so it runs outside of the ksampler pipelines.  I'd like to eventually add inpainting and ControlNet for `🤗 diffusers` but it will take some time.  This requires high amounts of VRAM (easily 18GB or more).  The following Fooocus configuration items are passed to the InstantID `🤗 diffusers` pipeline:

* Resolution (width and height)
* Prompt (and generated prompts from selected styles)
* Negative Prompt (and generated prompts from selected styles)
* Steps
* CFG/Guidance Scale
* Seed
* LoRAs
* Sampler (not fully implemented)
* Scheduler (not fully implemented)

### InstantID General Usage

1. Navigate to the InstantID tab.
2. Click "Enable"
3. Load images from your PC.
4. Enter your prompt and be sure to include "man img" or "woman img" depending on the subject at hand.  **img** in the prompt is expected by PhotoMaker.
5. Click "Generate"

Experiment with also adding an image to the Inswapper tab to overlay the generated image.

**Note: Unchecking "Enable" will unload the InstantID pipeline from memory!**

### InstantID LoRA Usage

1. Select the LoRAs you want to use as usual.
2. Navigate to the InstantID tab.
3. Click "Enable" then click "Generate"

If you change the LoRAs or their weights:

1. Uncheck "Enabled" to unload the model from memory
2. Re-check "Enabled" and click "Generate" to reload the LoRAs and the pipeline into memory.

### Supported InstantID samplers
* euler
* euler ancestral
* DPM++ 2M SDE
* DPM++ 2M SDE Karras
* Will default to DDIM Scheduler for anything else

## Colab

Note that the minimal requirement is **4GB Nvidia GPU memory (4GB VRAM)** and **8GB system memory (8GB RAM)**. This requires using Microsoft’s Virtual Swap technique, which is automatically enabled by your Windows installation in most cases, so you often do not need to do anything about it. However, if you are not sure, or if you manually turned it off (would anyone really do that?), or **if you see any "RuntimeError: CPUAllocator"**, you can enable it here:

<details>
<summary>Click here to see the image instructions. </summary>

![image](https://github.com/lllyasviel/Fooocus/assets/19834515/2a06b130-fe9b-4504-94f1-2763be4476e9)

**And make sure that you have at least 40GB free space on each drive if you still see "RuntimeError: CPUAllocator" !**

</details>

Please open an issue if you use similar devices but still cannot achieve acceptable performances.

Note that the [minimal requirement](#minimal-requirement) for different platforms is different.

See also the common problems and troubleshoots [here](troubleshoot.md).

### Switching from Fooocus to this fork

1. open a terminal in your Fooocus folder (the one with your config.txt)
2. execute `git status`. You should see the following:
    ```
    On branch main
    Your branch is up to date with 'origin/main'.
    
    nothing to commit, working tree clean
    ```
    If not, execute `git reset --hard origin/main` and check `git status` again.
3. execute
    ```
    git remote set-url origin https://github.com/mashb1t/Fooocus.git
    git pull
    ```
6. activate your venv (not necessary when installed from 7z) and update your python packages depending on your environment (7z, venv, conda, etc.)

   Example for Windows (7z): `..\python_embeded\python.exe -m pip install -r "requirements_versions.txt"`
8. start Fooocus either by opening the run.bat or corresponding entrypoint (same as before)

OR

Windows: download the [7z file](#download), extract it and run `run.bat`. You may want to copy over already downloaded checkpoints / LoRAs / etc.

### Colab

(Last tested - 2023 Dec 12)

| Colab | Info
| --- | --- |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mashb1t/Fooocus/blob/main/fooocus_colab.ipynb) | Fooocus Official

## Issues

Please report any issues in the Issues tab.  I will try to help as much as I can.

## To Do

1. 🚀 Allow changing of insightface parameters (Inswapper)
2. 🚀 [Allow customizable target image](https://github.com/machineminded/Fooocus-inswapper/issues/12) (Inswapper)
3. 🚀 Increase diffusers pipeline to > 77 tokens (PhotoMaker)
4. 🚀 Allow dynamic loading of LoRAs into diffusers pipeline (PhotoMaker)
