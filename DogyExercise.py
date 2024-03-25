"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()


api_key = os.getenv("GoogleAPI")



genai.configure(api_key=api_key)

def GetExercises(DogeSize,DogyEnergyLevel,DogySensitivity,DogyAge):
                
            # Set up the model
                generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
            }

                safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            ]

                model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                        generation_config=generation_config,
                                        safety_settings=safety_settings)

                prompt_parts = [
            f"input: Given the following characteristics of a dog:\n- Size: {DogeSize}\n- Energy Level: {DogyEnergyLevel}\n- Sensitivity: {DogySensitivity}\n- Age: {DogyAge}\n\nProvide a detailed exercise summary tailored for this dog. The summary should include recommendations on the type, duration, and intensity of exercise appropriate for the dog's size, energy level, sensitivity, and age. Consider the dog's physical and emotional well-being, ensuring the suggested activities promote health without causing undue stress or exhaustion.",
            f"output: Detailed Summary of Exercises for Dogy",
            f"input: dog:\n- Size: {DogeSize}\n- Energy Level: {DogyEnergyLevel}\n- Sensitivity: {DogySensitivity}\n- Age: {DogyAge}",
            f"output: ",
            ]

                response = model.generate_content(prompt_parts)
                return response.text


def GetExerciseswithlocation(DogeSize, DogyEnergyLevel, DogySensitivity, DogyAge, Latitude, Longitude):
    # Set up the model configuration
    generation_config = {
        "temperature": 0.7,  # Adjust for more predictable outputs
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    sensitivity_list = [key for key, value in DogySensitivity.dict().items() if value]
    sensitivities = ', '.join(sensitivity_list) if sensitivity_list else 'none'


    # Build the prompt
    prompt = (
        f"Given a dog with the following characteristics:\n"
        f"- Size: {DogeSize}\n"
        f"- Energy Level: {DogyEnergyLevel}\n"
        f"- Sensitivities: {sensitivities}\n"
        f"- Age: {DogyAge} years\n"
        f"- Location: Latitude {Latitude}, Longitude {Longitude}\n\n"
        "Provide a detailed exercise summary tailored for this dog. The summary should include "
        "recommendations on the type, duration, and intensity of exercise appropriate for the dog's "
        "size, energy level, sensitivities, and age. Also, suggest types of locations that are suitable "
        "for the dog to exercise in, considering its sensitivities and the geographical area.\n\n"
        "Output should include:\n"
        "- Exercise type\n"
        "- Exercise duration\n"
        "- Exercise intensity\n"
        "- Recommended location types for exercise"
    )

    # Generate content based on the prompt
    response = model.generate_content(prompt)
    return response.text


