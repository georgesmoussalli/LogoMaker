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
import random


_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

def get_most_centered_space_index(text):
    text_length = len(text)
    spaces_indices = [i for i in range(text_length) if text[i] == ' ']
    
    # return index of space that is closest to the center of the string
    return min(spaces_indices, key=lambda index: abs(text_length / 2 - index))

def title_splitter(title: TextObject, title_1 : TextObject, title_2 : TextObject):

    if ' ' not in title.content:
        # if there's no space in the title, return False and the original title objects
        return False
    else:
        split_flag = True #random.choice([True, False])
        
        if not split_flag:
            # if split flag is False, return False and the original title objects
            return False, title, title
        else:
            # split the title content at the most centered space
            split_index = get_most_centered_space_index(title.content)
            title_1.content, title_2.content = title.content[:split_index], title.content[split_index+1:]
            
            # adjust the position of the titles if needed
            # title_1.y += 10  # for example
            # title_2.y -= 10  # for example

            # return True and the new title objects
            return True



def generate_svg( background : BackgroundObject, title : TextObject ,slogan : TextObject, container_icon : IconObject, center_icon : IconObject, letter_icon : IconObject, splitted : bool, title_1 : TextObject, title_2 : TextObject) -> str :

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

title_1 = text_object.TextObject(
    content="",
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

title_2 = text_object.TextObject(
    content="",
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
            
center_icon.png_base64 = get_png_base64(center_icon.keyword, center_icon.color, 0, 2) 
splitted = title_splitter(title, title_1, title_2)
tab = apply_layout(background, title, slogan,center_icon, 6, title_1, title_2)
svg = generate_svg(background, title, slogan, container_icon, center_icon, letter_icon, splitted, title_1, title_2)    

with open(Path(str(_DIR_DATA) + "/_output_svg.svg"), 'w') as f:  
    f.write(svg)
