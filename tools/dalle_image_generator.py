from langchain_core.tools import tool
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

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
     )

    return response.data[0].url