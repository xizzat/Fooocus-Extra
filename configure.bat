@echo off
git clone https://github.com/haofanwang/inswapper.git
cd inswapper
git lfs install
git clone https://huggingface.co/spaces/sczhou/CodeFormer
cd ..
python -m venv venv
call .\venv\Scripts\activate
pip install -r requirements_versions.txt
pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
xcopy /E /I /Y inswapper\CodeFormer\CodeFormer\basicsr venv\Lib\site-packages\basicsr
xcopy /E /I /Y inswapper\CodeFormer\CodeFormer\facelib venv\Lib\site-packages\facelib
mkdir inswapper\checkpoints
powershell -Command "& { Invoke-WebRequest -Uri 'https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx' -OutFile '.\inswapper\checkpoints\inswapper_128.onnx' }"

mkdir InstantID\models
mkdir InstantID\models\antelopev2
powershell -Command "& { Invoke-WebRequest -Uri 'https://drive.google.com/file/d/18wEUfMNohBJ4K3Ly5wpTejPfDzp-8fI8/view?usp=sharing' -OutFile '.\InstantID\models\antelopev2.zip' }"

expand -F:* ".\InstantID\models\antelopev2.zip" ".\InstantID\models\antelopev2"