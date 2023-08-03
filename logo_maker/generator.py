from background_object import BackgroundObject
from get_font_file import get_font_file
from icon_object import IconObject
import os
from pathlib import Path
from string_to_path import string_to_svg_paths
from text_object import TextObject

_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

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
    template += string_to_svg_paths(slogan)
    
    template += """</g>
            <g id="title" style="font-size:{title.font_size};font-family:'{title.font}';text-anchor:{title.anchor}">
             
    """
    template +=  string_to_svg_paths(title)
        
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

    

