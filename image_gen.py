import openai
import os
from dotenv import load_dotenv
import requests
from PIL import Image

def img_gen():

  # Load environment variables from .env file
  load_dotenv()

  # Initialize OpenAI client with API key
  openai.api_key = os.getenv("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>")

  from openai import OpenAI
  client = OpenAI()

  print("Hello! Welcome to your museum. Give your thoughts. We generate an image, delete the words and store your work. ")
  # Prompts user for the image they wanna generate.
  print("What image do you want to generate?")


  response = client.images.generate(
    model="dall-e-3",
    prompt= input(),
    size="1024x1024",
    quality="hd",
    n=1,
  )
  #TODO: Need to be able to store multiple images in a DB but need to understand how big they will be. 1.6MB to 2 MB
  #TODO: FUCK THIS FUCKING LIFE WHAT THE FUCK MAN!!! 
  #TODO: Create DB to store at least 30 images for a month. 
  #TODO: NEED an ERD but it wouldn't be too b
  #TODO: Needs API endpoints; create new module(api.py)
  #TODO: Gonna go MVC. (Django)
  #TODO: Models? Gonna keep it simple first. let's setup the connection with the DB and frontend.
  #TODO: Image: Content, date



  print("Generating...")

  data = requests.get(response.data[0].url).content

  with open('img.png', 'wb') as f:
      f.write(data)



  img = Image.open(r"img.png")
  img.show()
  return img
