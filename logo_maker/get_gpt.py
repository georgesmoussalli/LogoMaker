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

# Get prompt
prompt = get_prompt_for_chatGPT()

# Get GPT's response to my prompt
def get_parameters() -> str:
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role" : "user", "content" : prompt }
        ]
    ) 
    print(response)