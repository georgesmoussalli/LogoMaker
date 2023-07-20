import base64
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables
_HERE = Path(os.path.abspath(__file__))
_DIR_ENV = _HERE.parent.parent.joinpath(".env")
load_dotenv(_DIR_ENV)

# Get API key and secret
NOUN_PROJECT_KEY = os.getenv("NOUN_PROJECT_KEY")
NOUN_PROJECT_SECRET = os.getenv("NOUN_PROJECT_SECRET")
auth = (OAuth1(NOUN_PROJECT_KEY,NOUN_PROJECT_SECRET))


def get_icon_id(keyword : str) -> list[str]: 
    parsed_data = requests.get("https://api.thenounproject.com/v2/icon?query=" + keyword + "&limit=4&thumbnail_size=200", auth=auth)
    print(parsed_data)
    parsed_data_json = parsed_data.json()
    print(parsed_data)
    icon_ids = [icon["id"] for icon in parsed_data_json["icons"]]
    return icon_ids

def get_png_base64(keyword : str, color ) -> list[str] : 
    list_png_base64 = []
    icon_ids = get_icon_id(keyword)
    for icon_id in icon_ids:
        parsed_data = requests.get("https://api.thenounproject.com/v2/icon/" + icon_id + "/download?color=" + color + "&filetype=png&size=200", auth=auth)
        print(parsed_data.content)
        parsed_data_json = parsed_data.json()
        list_png_base64.append(parsed_data_json["base64_encoded_file"])
        
    return list_png_base64

print(get_png_base64("banana", "FFFF00"))