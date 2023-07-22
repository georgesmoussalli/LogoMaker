from background_object import BackgroundObject
import base64 
from get_font_file import get_font_file
from icon_object import IconObject
import os
from pathlib import Path
from text_object import TextObject

_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

# SVG template for creation with all parameters but the icon 
template_1_code = """
<svg xmlns='http://www.w3.org/2000/svg' width='{background.width}' height='{background.height}'>
    <style>
        @font-face {{
            font-family: '{title.font}';
            src: url(data:font/ttf;base64,{title_font_data}) format('truetype');
        }}
        @font-face {{
            font-family: '{slogan.font}';
            src: url(data:font/ttf;base64,{slogan_font_data}) format('truetype');
        }}
    </style>
    <rect width='{background.width}' height='{background.height}' fill='{background.color}' />
    <text x='{title.x}%' y='{title.y}%' text-anchor='{title.anchor}' font-size='{title.font_size}' font-family='{title.font}' fill='{title.font_color}'>{title.content}</text>
    <text x='{slogan.x}%' y='{slogan.y}%' text-anchor='{slogan.anchor}' font-size='{slogan.font_size}' font-family='{slogan.font}' fill='{slogan.font_color}'>{slogan.content}</text>
</svg>
"""

# SVG template for creation with all parameters
template_2_code = """
<svg xmlns='http://www.w3.org/2000/svg' width='{background.width}' height='{background.height}'>
    <style>
        @font-face {{
            font-family: '{title.font}';
            src: url(data:font/ttf;base64,{title_font_data}) format('truetype');
        }}
        @font-face {{
            font-family: '{slogan.font}';
            src: url(data:font/ttf;base64,{slogan_font_data}) format('truetype');
        }}
    </style>
    <rect width='{background.width}' height='{background.height}' fill='{background.color}' />
    <text x='{title.x}%' y='{title.y}%' text-anchor='{title.anchor}' font-size='{title.font_size}' font-family='{title.font}' fill='{title.font_color}'>{title.content}</text>
    <text x='{slogan.x}%' y='{slogan.y}%' text-anchor='{slogan.anchor}' font-size='{slogan.font_size}' font-family='{slogan.font}' fill='{slogan.font_color}'>{slogan.content}</text>
    <image href="data:image/png;base64,{icon.png_base64}" x='{icon.x}%' y='{icon.y}%' width='{icon.width}%' height='{icon.height}%' />
</svg>
"""


def generate_svg(background : BackgroundObject, title : TextObject , slogan : TextObject, icon : IconObject, layout : int, template : int) -> str :
    

    if(template == 1) : 
        # Inject the font data into the SVG template
        svg_content = template_1_code.format(
            background=background,
            title=title,
            slogan=slogan,
            title_font_data=title.title_font_data_encoded,
            slogan_font_data=slogan.slogan_font_data_encoded
    )
    elif(template == 2) : 
        # Inject the font data into the SVG template
        svg_content = template_2_code.format(
            background=background,
            title=title,
            slogan=slogan,
            icon = icon,
            title_font_data=title.title_font_data_encoded,
            slogan_font_data=slogan.slogan_font_data_encoded
    )
    else : print(template)
    return svg_content

