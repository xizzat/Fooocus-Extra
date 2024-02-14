#!/bin/bash

# Clone the repository
git clone https://github.com/haofanwang/inswapper.git
cd inswapper

# Install Git LFS
git lfs install

# Clone the Hugging Face model
git clone https://huggingface.co/spaces/sczhou/CodeFormer

# Move back to the parent directory
cd ..

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements_versions.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Copy directories
echo "Copying basicsr"
cp -r inswapper/CodeFormer/CodeFormer/basicsr venv/lib/site-packages/
echo "Copying facelib"
cp -r inswapper/CodeFormer/CodeFormer/facelib venv/lib/site-packages/

# Create a directory for checkpoints
mkdir -p inswapper/checkpoints

# Download the ONNX model
wget https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx -O inswapper/checkpoints/inswapper_128.onnx

# Setup InstantID
mkdir -p InstantID/models/antelopev2
wget -O InstantID/models/antelopev2/antelopev2.zip 'https://drive.google.com/uc?export=download&id=18wEUfMNohBJ4K3Ly5wpTejPfDzp-8fI8'
unzip InstantID/models/antelopev2/antelopev2.zip -d InstantID/models/antelopev2
