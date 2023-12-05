import openai

class OpenAINode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A world without prompts"
                }),
                "api_url": ("STRING", {
                    "multiline": False,
                    "default": "http://127.0.0.1:5000/v1"
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "BadPanda"
                }),
                "temperature": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"
                }),
                "sys_prefix": ("STRING", {
                    "multiline": True,
                    "default": "You are a prompt generation AI. your task is to take a user input for a stable difusion prompt and output and expand the supplied prompt in a stable difusion format to provide better output. Do not deviate from the format. Do not output anything other than a stable diffusion prompt."
                }),
                "stop_token": ("STRING", {
                    "multiline": False,
                    "default": "<|im_end|>"
                }),
                "max_tokens": ("INT", {
                        "default": 250,
                        "min": -1, 
                        "max": 2048,
                        "display": "number"
                }),
                "seed": ("INT", {
                        "default": 0,
                        "min": 0, 
                        "max": 0xffffffffffffffff
                })
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "get_completion"

    CATEGORY = "OpenAIapi"

    def get_completion(self, prompt, api_url, api_key, temperature, sys_prefix, stop_token, max_tokens, seed, model="local model"):
        try:
            openai.api_base = api_url
            openai.api_key = api_key

            
            messages = [{"role": "system", "content": sys_prefix},{"role": "user", "content": prompt}]
            
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stop=stop_token,
            )

            return (response.choices[0].message["content"],)

        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
            return ("Bad Panda",)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OpenAINode": OpenAINode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenAINode": "OpenAI Node"
}

