from dotenv import load_dotenv
import os
from pathlib import Path 

_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")
file = open(str(_DIR_DATA) + "/prompt.txt")


def get_prompt_for_chatGPT():   
    prompt = file.read() 
    return prompt
