from langchain_core.tools import tool
from langchain_openai import OpenAI
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

@tool
def generate_dalle_image(prompt: str):
    """
    Function to generate an image using OpenAI's DALL-E model.

    Parameters:
    - prompt (str): The prompt to generate the image.

    Returns:
    - str: The URL of the generated image.
    """
    client = OpenAI()
    
    image_url = DallEAPIWrapper().run(prompt)

    return image_url