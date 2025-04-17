from google import genai
import os
from django.conf import settings
import json

API_KEY = settings.GOOGLE_API_KEY 

client = genai.Client(api_key=API_KEY)


def analyze_text_with_gemini(prompt):
    full_response = ''
    for chunk in client.models.generate_content_stream(
        model='gemini-2.0-flash',
        contents=f"""You are an assistant that extracts tone and intent.
Given the user message: "{prompt}", return JSON with keys 'tone' and 'intent'.
Respond ONLY in this JSON format:
{{"tone": "...", "intent": "..."}}"""
   ):
        
        full_response += chunk.text
        
    try:
        full_response = full_response.strip().strip('```json').strip('```')
        return json.loads(full_response)
    except Exception as e:
        print("Error:",e)
        return {"tone":"unknown","intend":"unknown"}

    
