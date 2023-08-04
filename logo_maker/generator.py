from background_object import BackgroundObject
import os
from pathlib import Path
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
        <g id="logo-center" transform="translate({title.group_x},{title.group_y})">   
            <image xlink:href="data:image/png;base64,{letter_icon.png_base64}" id="icon_center" x="{letter_icon.x}" y="{letter_icon.y}" width="{letter_icon.width}" height="{letter_icon.height}" transform="translate{letter_icon.translate} scale({letter_icon.scale})"></image>
            <g id="slogan" style="font-size:{slogan.font_size};font-family:'{slogan.font}'">
            """
    template += tab[2]
    
    template += """</g>
            <g id="title" style="font-size:{title.font_size};font-family:'{title.font}'">
             
    """
    template += tab[1]
        
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
    content="Content",
    font_size= None,
    font = "Aleo-Bold",
    x = 0,
    y = 0,
    font_color= "#AA11AA",
    text_font_data_encoded= None,
    anchor = None,
    scale_factor= None,
    width = 0,
    group_x = None,
    group_y = None
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
    group_x= None,
    group_y= None
    
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

tab = apply_layout(background, title, slogan,center_icon, 1)
svg = generate_svg(background, title, slogan, container_icon, center_icon, letter_icon)    
with open(Path(str(_DIR_DATA) + "/_output_svg.svg"), 'w') as f:  
    f.write(svg)
