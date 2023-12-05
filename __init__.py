# __init__.py

from .openai_node import OpenAINode

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OpenAINode": OpenAINode
}
