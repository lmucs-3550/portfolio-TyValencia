# Ty Valencia
# CMSI3550

import os
import openai
import random
from PIL import Image
from pathlib import Path
from difflib import get_close_matches

# Configure the OpenAI API
openai.organization = "org-1pupknsOnOoA1T7a5tZNuxtU"
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_image_keywords(image_path):
    with open(image_path, "rb") as image_file:
        response = openai.Image.create_keywords(image_file)
    keywords = response["data"]["keywords"]
    return keywords

def generate_keywords_dict(images_folder):
    keywords_dict = {}
    for img_path in images_folder.glob("*.png") + images_folder.glob("*.jpg"):
        keywords = get_image_keywords(img_path)
        keywords_dict[img_path] = keywords
    return keywords_dict

def get_relevant_images(prompt, keywords_dict):
    prompt_words = prompt.lower().split()
    relevant_images = set()
    for img_path, keywords in keywords_dict.items():
        for word in prompt_words:
            close_matches = get_close_matches(word, keywords, n=1, cutoff=0.5)
            if close_matches:
                relevant_images.add(img_path)
                break
    return relevant_images

def generate_image(images_folder, prompt, relevant_images):
    if not relevant_images:
        print("No relevant images found.")
        return

    base_image_path = random.choice(list(relevant_images))
    with open(base_image_path, "rb") as image_file:
        response = openai.Image.create_edit(
            image=image_file,
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
    image_url = response["data"][0]["url"]

    generated_image_path = images_folder / f"generated_image.png"
    with open(generated_image_path, "wb") as f:
        f.write(openai.api_client.download(url=image_url).content)

    return generated_image_path

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing images: ")
    images_folder = Path(folder_path).resolve()

    if not images_folder.is_dir():
        print(f"{folder_path} is not a valid directory.")
        exit()

    print("Generating keywords dictionary...")
    keywords_dict = generate_keywords_dict(images_folder)

    prompt = input("Enter a prompt for the image generation: ")

    relevant_images = get_relevant_images(prompt, keywords_dict)
    generated_image_path = generate_image(images_folder, prompt, relevant_images)
    if generated_image_path:
        print(f"Generated image saved at: {generated_image_path}")