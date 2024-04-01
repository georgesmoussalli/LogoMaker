from dotenv import load_dotenv
from get_prompt import get_prompt_for_chatGPT
import json
import openai 
import os 
from pathlib import Path

# Get API key 
_HERE = Path(os.path.abspath(__file__))
_DIR_ENV = _HERE.parent.parent.joinpath(".env")
load_dotenv(_DIR_ENV)
openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo-0125"

# Get prompt
prompt = get_prompt_for_chatGPT()

def get_GPT_prompt() : 
    return prompt
def get_model() : 
    return model

# Puts all the data lowercase
def lowercase_keys(data : dict) -> dict:
    if isinstance(data, dict):
        return {key.lower(): lowercase_keys(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [lowercase_keys(item) for item in data]
    else:
        return data

# Get GPT's response to my prompt
def get_parameters() -> str:
    my_openai_obj = openai.ChatCompletion.create(
        model = model,
        messages = [
            {"role" : "user", "content" : prompt }
        ]
    )   
    response = list(my_openai_obj.choices)[0]
    response = response.to_dict()['message']['content']
    python_object = lowercase_keys(json.loads(response))
    return python_object
