#!/bin/sh


# GPU INSTALL ONLY

pkgs=(
  "huggingface_hub" 
  "python-dotenv" "openai"
  "torch torchvision torchaudio"
  "bitsandbytes" 
  "gradio"
   "accelerate"
  "transformers==4.30"
  "git+https://github.com/huggingface/accelerate"
  # if you run into issues you can run these after making sure your device is cuda enabled. 
  # Torch needs to match your cuda/libcuda.so version.
  # transformers needs to be 4.30 on my device
  # "git+https://github.com/huggingface/transformers"
  # "git+https://github.com/huggingface/bitsandbytes"
  # "git+https://github.com/huggingface/peft.git"

)  

for pkg in "${pkgs[@]}"; do
  echo -e "\n\x1B[96m  INSTALLING:   $pkg \x1B[0m"
  pip install $pkg --upgrade
done


# if you run into issues you can run these after making sure your device is cuda enabled. Torch needs to match your cuda/libcuda.so version.
# pip install -q -U bitsandbytes
# pip install -q -U git+https://github.com/huggingface/transformers.git
# pip install -q -U git+https://github.com/huggingface/peft.git
# pip install -q -U git+https://github.com/huggingface/accelerate.git



