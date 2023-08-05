from background_object import BackgroundObject
import os
from pathlib import Path
import text_object
import icon_object
import background_object
from text_object import TextObject
from icon_object import IconObject
from layout import apply_layout
from get_noun_project import get_png_base64



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
        <image href="data:image/png;base64,{center_icon.png_base64}" x='{center_icon.x}' y='{center_icon.y}' width='{center_icon.width}' height='{center_icon.height}' transform=" scale({letter_icon.scale})"/>
        <g id="title-container" transform="translate({title.group_x},{title.group_y})">   
            <g id="title" style="font-size:{title.font_size};font-family:'{title.font}'">
            """
    template += tab[1]
    
    template += """</g>
        </g>
        <g id="slogan-container" transform="translate({slogan.group_x},{slogan.group_y})">   
            <g id="slogan" style="font-size:{slogan.font_size};font-family:'{slogan.font}'">
             
    """
    template += tab[2]
        
    template += """</g>
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
    content="Coffee Inc.",
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
    content="Coffee is best served with us",
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
    scale = 1
    )


center_icon = icon_object.IconObject(
    color = "AA11AA",
    x = 0,
    y = 0,
    width = 20,
    height = 20,
    keyword = "Coffee",
    png_base64 = None,
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
    scale = 1
    )
            
center_icon.png_base64 = get_png_base64(center_icon.keyword, center_icon.color, 1, 2)
tab = apply_layout(background, title, slogan,center_icon, 2)
svg = generate_svg(background, title, slogan, container_icon, center_icon, letter_icon)    
with open(Path(str(_DIR_DATA) + "/_output_svg.svg"), 'w') as f:  
    f.write(svg)
