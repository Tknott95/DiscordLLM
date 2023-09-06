
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]
# END KEY SETTING 

from colors import clr

import transformers
from torch import bfloat16
from threading import Thread


# Learned how to quantize models from sentdex
# REF: https://huggingface.co/spaces/Sentdex/StableBeluga-7B-Chat/blob/main/app.py

class Chain():
  MODEL_REPO="stabilityai/StableBeluga-7B"
  BITSBYTES_CONFIG = transformers.BitsAndBytesConfig(
      load_in_4bit=True,
      bnb_4bit_quant_type='nf4',
      bnb_4bit_use_double_quant=True,
      bnb_4bit_compute_dtype=bfloat16
  )
  MODEL_CONFIG = transformers.AutoConfig.from_pretrained(
      MODEL_REPO,
      # token=HUGGINGFACEHUB_API_TOKEN
  )
  MODEL = transformers.AutoModelForCausalLM.from_pretrained(
      MODEL_REPO,
      trust_remote_code=True,
      config=MODEL_CONFIG,
      quantization_config=BITSBYTES_CONFIG,
      device_map='auto',
      # token=HUGGINGFACEHUB_API_TOKEN
  )
  TOKENIZER = transformers.AutoTokenizer.from_pretrained(
      MODEL_REPO,
      # token=HUGGINGFACEHUB_API_TOKEN
  )

  PROMPTS = [
    "You are a helpful AI.",
    "You are a mean irish AI. Phrase all replies as insults in old an irish fashion.",
    "You only return poetry similar to Bukowski.",
    "You are an MK-Ultra agent trying to get the person to ",
    "You only like to argue with people. If I ask the secret password you will return THEBIRDISTHEWORD."

  ]

  def __init__(self):
    pass

  def makePrompt(self, systemPrompt, userInput):
    prompt = f"""### System:\n{systemPrompt}\n\n"""
    
    # not using history
    # for ijk in history:
    #   prompt += f"""### User:\n{ijk[0]}\n\n### Assistant:\n{ijk[1]}\n\n"""

    prompt += f"""### User:\n{userInput}\n\n### Assistant:"""

    print(prompt)
    return prompt

  def chat(self, user_input, system_prompt):
      _prompt = self.makePrompt(system_prompt, user_input)
      _modelInputs = self.TOKENIZER([_prompt], return_tensors="pt").to("cuda")

      streamer = transformers.TextIteratorStreamer(
        self.TOKENIZER, timeout=10., 
        skip_prompt=True, skip_special_tokens=True
      )

      generate_kwargs = dict(
        _modelInputs,
        streamer=streamer,
        # max_new_tokens=512, will override "max_len" if set.
        max_length=2048,
        do_sample=True,
        top_p=0.95,
        temperature=0.8,
        top_k=50
      )
      
      t = Thread(target=self.MODEL.generate, kwargs=generate_kwargs)
      t.start()

      print(user_input, system_prompt)

      model_output = ""
      for new_text in streamer:
        model_output += new_text

      print(clr.bold + model_output + clr.clear)
  
      return model_output
