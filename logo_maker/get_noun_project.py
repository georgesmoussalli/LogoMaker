from dotenv import load_dotenv
from pathlib import Path
import os
import requests
from requests_oauthlib import OAuth1

# Load environment variables
_HERE = Path(os.path.abspath(__file__))
_DIR_ENV = _HERE.parent.parent.joinpath(".env")
load_dotenv(_DIR_ENV)

# Get API key and secret
NOUN_PROJECT_KEY = os.getenv("NOUN_PROJECT_KEY")
NOUN_PROJECT_SECRET = os.getenv("NOUN_PROJECT_SECRET")
auth = (OAuth1(NOUN_PROJECT_KEY,NOUN_PROJECT_SECRET))


def get_icon_ids(keyword : str, limit : int) -> list[str]: 
    parsed_data = requests.get("https://api.thenounproject.com/v2/icon?query=" + keyword + "&limit=" + str(limit) + "&thumbnail_size=200&include_svg=0&limit_to_public_domain=1", auth=auth)
    parsed_data_json = parsed_data.json()
    icon_ids = [icon["id"] for icon in parsed_data_json["icons"]]
    return icon_ids

def get_png_base64(keyword : str, color  :str, i : int, limit : int ) -> str : 
    icon_ids = get_icon_ids(keyword, limit)
    parsed_data = requests.get("https://api.thenounproject.com/v2/icon/" + icon_ids[i] + "/download?color=" + color + "&filetype=png&size=200", auth=auth)
    parsed_data_json = parsed_data.json()
        
    return parsed_data_json["base64_encoded_file"]
    