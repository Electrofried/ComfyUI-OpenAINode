# OpenAINode

A simply node for hooking in to openAI API based servers via comfyUI

## Description

I just wanted to feed basic prompts through a local hosted LLM. Nothing I could find did this, so I got the LLM (with a bit of prodding) to make a node for me! This should allow you to hook in to any local hosted LLM that has openAI API support and run inferance on a string then get a string back.


## Getting Started

Load up your LLM of choice, with your model of choice, in your launcher of choice (Ooba, LLM studio and many more support this). Plop down the node, enter the URL in the node and alter the prefix, suffix and any stop token your model uses. Job done.
I am working on a small 7B model on huggingface I have dubbed [promptmaster-mistral7b](https://huggingface.co/Electrofried/Promptmaster-mistral-7b) that is fine tuned with the default perameters to output stable diffusion style prompts. It is very WIP right now and while it 'works' I would not call it 'good', more refinment to come. 

It is however fun to use and when it does work it works really well to convert basic input like "a photo of a woman in a cyberpunk world" into "photorealistic, the portrait of a female sitting with cyberpunk clothes, gray bun, REDACTED, wide hips, dark REDACTED hair, focus on her REDACTED, cab, CamoGoal girl bridge with light, crowded outside city leaves, (cyberpunk-themed), dark atmosphere, deep shadow, dimly lit, dark studio, low key, urban decay, neon light, deep contrast, moody, film noir aesthetic, cyber goth, cyberpunk edgerunners"


Oh, I should also mention, that model... See those "REDACTED"... yea, it has been trained on all kinds of prompts so expect NSFW output to randomly pop up. You have been warned.

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
