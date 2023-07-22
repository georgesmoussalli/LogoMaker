import base64
import os
from pathlib import Path
from text_object import TextObject


_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

def get_font_file(title : TextObject, slogan : TextObject ) : 
    font_formats = [".otf", ".ttf"]
    title_font_data = None
    slogan_font_data = None

    for font_format in font_formats:
        try:
            with open(str(_DIR_DATA) + "/fontsMVP/" + title.font + font_format, "rb") as title_font_file:
                title_font_data = title_font_file.read()
            with open(str(_DIR_DATA)+ "/fontsMVP/" + slogan.font + font_format, "rb") as slogan_font_file:
                slogan_font_data = slogan_font_file.read()
            break  # If opening the font files succeeds, exit the loop
        except FileNotFoundError:
            continue  # If font files are not found, try the next format

    if title_font_data is None or slogan_font_data is None:
        raise FileNotFoundError("Font files not found for title or slogan.")

    # Encode the font data in base64
    title.title_font_data_encoded = base64.b64encode(title_font_data).decode("utf-8")
    slogan.slogan_font_data_encoded = base64.b64encode(slogan_font_data).decode("utf-8")