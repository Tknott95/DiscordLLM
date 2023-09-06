# TOC_DISCORD_BOT
# DiscordLLM

By using model quantization you can run larger llms on your device that was not possible prior. Learn more about hardware needed without model quantization here: https://www.hardware-corner.net/guides/computer-to-run-llama-ai-model/

This DiscordBot uses StableBeluga7B for this example and does not remember history as it is meant to be a one shot answer in whatever specialized prompt you would like. In the future history can be brought back or you could extend this yourself.

**LEARNED about model quantization from sentdex(code is only on huggingface)** 
##### REF: https://huggingface.co/spaces/Sentdex/StableBeluga-7B-Chat/blob/main/app.py



**HUGGING FACE OPEN SOURCE LLM LEADERBOARDS**
https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

**MODEL QUNATIZATION**
https://huggingface.co/docs/transformers/main_classes/quantization





**TURN INTO A TERMINAL BOT**
```
def main():
  print("\n\n  LLMAgents init()\n")

  _chain = Chain()
  isAsking = True
  # _chain.chat("What color is the sun?", _chain.PROMPTS[0])

  while(isAsking):
    _input = input(clr.bar + "\n  Want to know anything?\n :  " + clr.clear)
    if(_input == "no"):
      isAsking = False
      print(clr.bold + "\n  Bot is going back to hibernation." + clr.clear) 
      break
    
    _chain.chat(_input, _chain.PROMPTS[0])



if __name__ == "__main__":
  main()

```