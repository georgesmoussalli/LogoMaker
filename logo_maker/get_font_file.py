import base64
import os
from pathlib import Path
from text_object import TextObject


_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

def get_font_file(text : TextObject) : 
    font_formats = [".otf", ".ttf"]
    text_font_data = None
    
    for font_format in font_formats:
        try:
            with open(str(_DIR_DATA) + "/fontsMVP/" + text.font + font_format, "rb") as text_font_file:
                text_font_data = text_font_file.read()
            break  # If opening the font files succeeds, exit the loop
        except FileNotFoundError:
            continue  # If font files are not found, try the next format

    if text_font_data is None:
        raise FileNotFoundError("Font files not found for text.")

    # Encode the font data in base64
    return base64.b64encode(text_font_data).decode("utf-8")
