import openai

class OpenAINode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": False,
                    "default": "A world without prompts"
                }),
                "api_base": ("STRING", {
                    "multiline": False,
                    "default": "http://192.168.1.65:5000/v1"
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
                "prefix": ("STRING", {
                    "multiline": False,
                    "default": "<|im_start|>system\nYou are a prompt generation AI. your task is to take a user input for a stable difusion prompt and output and expand the supplied prompt in a stable difusion format to provide better output. Do not deviate from the format. Do not output anything other than a stable diffusion prompt.<|im_end|>\n<|im_start|>user\n"
                }),
                "suffix": ("STRING", {
                    "multiline": False,
                    "default":  "<|im_end|>\n<|im_start|>assistant\n"
                }),
                "stop": ("STRING", {
                    "multiline": False,
                    "default": "<|im_end|>"
                }),
                "seed": ("INT", {
                        "default": 0, "min": 0, 
                        "max": 0xffffffffffffffff
                })
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "get_completion"

    CATEGORY = "OpenAIapi"

    def get_completion(self, prompt, api_base, api_key, temperature, prefix, suffix, stop, seed, model="local model"):
        try:
            openai.api_base = api_base
            openai.api_key = api_key

            formatted_prompt = f"{prefix}{prompt}{suffix}"
            messages = [{"role": "user", "content": formatted_prompt}]
            
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                stop=stop,
                early_stopping=True
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
