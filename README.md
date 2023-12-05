# OpenAINode

A simply node for hooking in to openAI API based servers via comfyUI

## Description

I just wanted to feed basic prompts through a local hosted LLM. Nothing I could find did this, so I got the LLM (with a bit of prodding) to make a node for me! This should allow you to hook in to any local hosted LLM that has openAI API support and run inferance on a string then get a string back.


## Getting Started

Load up your LLM of choice, with your model of choice, in your launcher of choice (Ooba, LLM studio and many more support this). Plop down the node, enter the URL in the node and alter the prefix, suffix and any stop token your model uses. Job done.
I am working on a small 7B model on huggingface I have dubbed [promptmaster-mistral7b](https://huggingface.co/Electrofried/Promptmaster-mistral-7b) that is fine tuned with the default perameters to output stable diffusion style prompts. It is very WIP right now and while it 'works' I would not call it 'good', more refinment to come. 

It is however fun to use and when it does work it works really well to convert basic input like "a photo of a woman in a cyberpunk world" into "photorealistic, the portrait of a female sitting with cyberpunk clothes, gray bun, REDACTED, wide hips, dark REDACTED hair, focus on her REDACTED, cab, CamoGoal girl bridge with light, crowded outside city leaves, (cyberpunk-themed), dark atmosphere, deep shadow, dimly lit, dark studio, low key, urban decay, neon light, deep contrast, moody, film noir aesthetic, cyber goth, cyberpunk edgerunners"

![workflow](https://github.com/Electrofried/ComfyUI-OpenAINode/assets/27886155/58df1e7b-4259-42f5-815d-df88be812695)


## WARNING WARNING WARNING!!!! WARNING WARNING WARNING!!!!  WARNING WARNING WARNING!!!!

The model I listed above is like a thirsty kid from 4chan who forgot to take their meds. I am not joking when I say it can and will add random totally NSFW/NSFL combinations of things to your prompt. Take care who/where/how you use this. I am not responsible if the LLM hijacks your prompt for "a baby panda" in the middle of a discord stream and you get a picture of "a panda with breasts sitting on a bamboo spike"... or worse.

## WARNING WARNING WARNING!!!! WARNING WARNING WARNING!!!!  WARNING WARNING WARNING!!!!

### Dependencies

openai  -  required for API calls. This will not work with the actual openAI (chatgpt) servers and not something I plan on supporting.

### Installing
```
git clone https://github.com/Electrofried/ComfyUI-OpenAINode
```
to your custom nodes folder and then 
```
pip -r install requirments.txt
```
### Executing program

* Drop the node in
* set the URL in api_url to your LLM server url
* convert your clip encoder to input by right clicking it
* do the same for the prompt input and create a new string node to connect it
* enter your prompt
* start a run


## Help

The seed input is there to allow a random seed to be input, this does not actually do anything to the seed. create a new primitive node and connect it to the seed then randomise each run. This will cause ComfyUI re re-prompt the LLM each time you run generation if you want to vary your prompt a bit. If you leave it set, then comfyUI will cache the results and use the same prompt each time it runs till you change the input.

A note on running this locally. Please take in to account running something like an LLM and stable diffusion at the same time on the same machine is going to be taxing. You will make your GPU cry if you try do this. Instead consider loading the LLM to RAM (if you have enough) and running inference via CPU then allowing stable diffusion to use the full GPU. Or, better yet hijack andother computer in your home and host the LLM inference there, then connect to it remotly as I do. Please do not raise an issue that you run out of memory when using this node or you will make the AI gods cry.
