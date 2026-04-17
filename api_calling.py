from google import genai 
from dotenv import load_dotenv
from gtts import gTTS
import os

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



prompt1 ="""From given images you will give 3 short lines  hints with points to fix the code
"""
prompt2="""Analyzing the images you will just give the corrected code
"""

def for_hints(images):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images,prompt1]
    )
    return response.text

def for_solution(images):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images,prompt2]
    )
    return response.text



