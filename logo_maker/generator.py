from background_object import BackgroundObject
from get_font_file import get_font_file
import os
from pathlib import Path
from string_to_path import string_to_svg_paths
import text_object
import icon_object
import background_object
from text_object import TextObject
from icon_object import IconObject
from layout import apply_layout


_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")


def font_size_selector( text : TextObject, background : BackgroundObject) -> int :
    # Calculate the initial font size based on the ratio of logo width to text length
    initial_font_size = int(background.width / len(text.content))
    
    # Limit the font size to the specified range
    font_size = max(min(initial_font_size, 70), 10)   
    print(font_size)
    return font_size

def vertical_space_text(text : TextObject):
    return text.y +  0.75 * text.font_size

def font_size_to_scale(font_size : int, font_size_range : range, scale_range : range) -> float : 
    min_font_size, max_font_size = font_size_range
    min_scale, max_scale = scale_range

    if font_size < min_font_size:
        return min_scale
    if font_size > max_font_size:
        return max_scale

    scale = min_scale + ((font_size - min_font_size) / (max_font_size - min_font_size)) * (max_scale - min_scale)
    return scale

def generate_svg( background : BackgroundObject, title : TextObject ,slogan : TextObject, container_icon : IconObject, center_icon : IconObject, letter_icon : IconObject) -> str :

    template = """
<svg xmlns='http://www.w3.org/2000/svg' width='{background.width}' height='{background.height}'>
    <style>
        @font-face {{
            font-family: '{title.font}';
            src: url(data:font/ttf;base64,{title.text_font_data_encoded}) format('truetype');
        }}
        @font-face {{
            font-family: '{slogan.font}';
            src: url(data:font/ttf;base64,{slogan.text_font_data_encoded}) format('truetype');
        }}
    </style>
    
    <rect width='{background.width}' height='{background.height}' fill='{background.color}' />
    <g id="logo-group">
        <image xlink:href="data:image/png;base64,{container_icon.png_base64}" id="container" x="{container_icon.x}" y="{container_icon.y}" width="{container_icon.width}" height="{container_icon.height}" transform="translate{container_icon.translate} scale({letter_icon.scale})"></image>
        <g id="logo-center" transform="translate({title.center_x},{title.center_y})">   
            <image xlink:href="data:image/png;base64,{letter_icon.png_base64}" id="icon_center" x="{letter_icon.x}" y="{letter_icon.y}" width="{letter_icon.width}" height="{letter_icon.height}" transform="translate{letter_icon.translate} scale({letter_icon.scale})"></image>
            <g id="slogan" style="font-size:{slogan.font_size};font-family:'{slogan.font}';text-anchor:{slogan.anchor}">
            """
    template += slogan_paths
    
    template += """</g>
            <g id="title" style="font-size:{title.font_size};font-family:'{title.font}';text-anchor:{title.anchor}">
             
    """
    template += title_paths
        
    template += """</g>
            <image href="data:image/png;base64,{center_icon.png_base64}" x='{center_icon.x}' y='{center_icon.y}' width='{center_icon.width}' height='{center_icon.height}' transform="translate{container_icon.translate} scale({letter_icon.scale})"/>
        </g>
    </g>
        
</svg>
"""
    
    svg_content = template.format(
            background=background,
            title=title,
            slogan=slogan, 
            container_icon = container_icon,
            center_icon = center_icon,
            letter_icon = letter_icon
        )
    return svg_content


background = background_object.BackgroundObject(
    color = "#AAAAAA",
    width = 400,
    height = 300
)

title = text_object.TextObject(
    content="C",
    font_size= None,
    font = "Aleo-Bold",
    x = 0,
    y = 0,
    font_color= "#AA11AA",
    text_font_data_encoded= None,
    anchor = None,
    scale_factor= None,
    width = 0,
    center_x= None,
    center_y=None
)

slogan = text_object.TextObject(
    content="C",
    font_size= None,
    font = "Aleo-Bold",
    x = 0,
    y = 0,
    font_color= "#AA11AA",
    text_font_data_encoded= None,
    anchor = None,
    scale_factor= None,
    width = 0,
    center_x= None,
    center_y=None
    
)

container_icon = icon_object.IconObject(
    color = None,
    x = -100000,
    y = -100000,
    width = 20,
    height = 20,
    keyword = None,
    png_base64 = None,
    translate = (0,0), 
    scale = 1
    )


center_icon = icon_object.IconObject(
    color = "#A111AA",
    x = -100000,
    y = -100000,
    width = 20,
    height = 20,
    keyword = None,
    png_base64 = None,
    translate = (0,0), 
    scale = 1
    )

letter_icon = icon_object.IconObject(
    color = None,
    x = -100000,
    y = -100000,
    width = 20,
    height = 20,
    keyword = None,
    png_base64 = None,
    translate = (0,0), 
    scale = 1
    )

font_size_range = (10, 70)  # This means that font sizes go from 10 to 20
scale_range = (0.015, 0.1)  # This means that scales go from 1.0 to 2.0
title.font_size = font_size_selector(title, background)
slogan.y = vertical_space_text(title)
title.scale_factor = font_size_to_scale(title.font_size, font_size_range, scale_range)
if(slogan.content != "") :     
    slogan.font_size = min(font_size_selector(slogan, background), title.font_size)
    slogan.scale_factor = font_size_to_scale(slogan.font_size, font_size_range,scale_range )
title.text_font_data_encoded = get_font_file(title)
slogan.text_font_data_encoded = get_font_file(slogan)
slogan_paths = string_to_svg_paths(slogan)
title_paths = string_to_svg_paths(title)
apply_layout(background, title, slogan,center_icon, 1)
svg = generate_svg(background, title, slogan, container_icon, center_icon, letter_icon)    
with open(Path(str(_DIR_DATA) + "/_output_svg.svg"), 'w') as f:  
    f.write(svg)
