from background_object import BackgroundObject
import base64
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


def vertical_space_text(y, font_size, max_height):
    return y +  150 * font_size / max_height

def vertical_space_icon_to_text(y, font_size, max_height):
    return y +  100 * font_size / max_height

# add other layout with icon in the middle or instead of a letter or in the background or add a form in the background
def apply_layout(background : BackgroundObject, title : TextObject , slogan : TextObject, icon : IconObject, layout : int,) -> int : 
    if layout == 1 :
     
        title.x = 50
        slogan.x = 50
        #slogan.font_size = title.font_size / 2.5
        title.y = 50 + 50 * ((title.font_size - (title.font_size / 2))/background.height)
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)
        title.anchor = "middle"
        slogan.anchor = "middle"
        return 1

    elif layout == 2 : 
        icon.x = 50 - icon.width/2
        icon.y = 50 - icon.height
        title.x = 50
        slogan.x = 50
        title.y = vertical_space_icon_to_text(icon.y, title.font_size, background.height) + icon.height
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)    
        title.anchor = "middle"
        slogan.anchor = "middle"
        return 2
    
    elif layout == 3 : 
        icon.x = 50 -  icon.width * 3/2
        icon.y = 50 - icon.height/2
        title.x = icon.x + icon.width
        slogan.x = title.x 
        title.y = 50 + 50 * ((title.font_size - (title.font_size / 2))/background.height)
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)    
        title.anchor = "start"
        slogan.anchor = "start" 
        return 2



def generate_svg(background : BackgroundObject, title : TextObject , slogan : TextObject, icon : IconObject, layout : int) -> str :
    
    #Check if title is 2 words
    #boolean = splitter(brand_name, title, title2)

    #Chose and apply layout
    #layoutHelper.layout = LS.choose_layout()

    template = apply_layout(background, title, slogan, icon, layout)

     # Read the font files as binary data
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
    title_font_data_encoded = base64.b64encode(title_font_data).decode("utf-8")
    slogan_font_data_encoded = base64.b64encode(slogan_font_data).decode("utf-8")

    if(template == 1) : 
        # Inject the font data into the SVG template
        svg_content = template_1_code.format(
            background=background,
            title=title,
            slogan=slogan,
            title_font_data=title_font_data_encoded,
            slogan_font_data=slogan_font_data_encoded
    )
    elif(template == 2) : 
        # Inject the font data into the SVG template
        svg_content = template_2_code.format(
            background=background,
            title=title,
            slogan=slogan,
            icon = icon,
            title_font_data=title_font_data_encoded,
            slogan_font_data=slogan_font_data_encoded
    )
    else : print(template)
    return svg_content

