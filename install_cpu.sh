#!/bin/sh

# CPU INSTALL ONLY
pkgs=(
  "huggingface_hub" 
  "python-dotenv" "openai"
  "torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu"
  "bitsandbytes" 
  "gradio"
  "accelerate>=0.20.3"
  "transformers==4.30"
  "flask"
  # transformers needs to be to be 4.30 for now
  # "git+https://github.com/huggingface/transformers"
)  

for pkg in "${pkgs[@]}"; do
  echo -e "\n\x1B[96m  INSTALLING:   $pkg \x1B[0m"
  pip install $pkg
done
