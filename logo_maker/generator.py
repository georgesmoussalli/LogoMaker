from background_object import BackgroundObject
import os
from pathlib import Path
from text_object import TextObject
from icon_object import IconObject


_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")


def generate_svg( background : BackgroundObject, title : TextObject ,slogan : TextObject, container_icon : IconObject, center_icon : IconObject, letter_icon : IconObject, splitted : bool, title_1 : TextObject, title_2 : TextObject, tab) -> str :

    if(splitted == False) : 
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
    elif(splitted == True) : 
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
                    <g id="title_1-container" transform="translate({title_1.group_x},{title_1.group_y})">   
                        <g id="title_1" style="font-size:{title_1.font_size};font-family:'{title_1.font}'">
                        """
        template += tab[1]
    
        template += """</g>
            </g>
                    <g id="title_2-container" transform="translate({title_2.group_x},{title_2.group_y})">   
                        <g id="slogan" style="font-size:{title_2.font_size};font-family:'{title_2.font}'">
             
         """
        template += tab[2]

        template += """</g>
            </g>
                    <g id="slogan-container" transform="translate({slogan.group_x},{slogan.group_y})">   
                        <g id="slogan" style="font-size:{slogan.font_size};font-family:'{slogan.font}'">
             
         """
        template += tab[3]
        
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
        letter_icon = letter_icon,
        title_1 = title_1,
        title_2 = title_2
        )

    return svg_content
