import background_object
from datetime import datetime
from generator import generate_svg
from get_font_file import get_font_file
import get_gpt
from get_noun_project import get_png_base64
import icon_object
from layout import apply_layout
import numpy as np
import os
from pathlib import Path
import select_random as sel
import text_object
import random

random.seed(0)
icon_number = 6
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
_HERE = Path(os.path.abspath(__file__))

data = get_gpt.get_parameters()
print(data)


def get_most_centered_space_index(text):
    text_length = len(text)
    spaces_indices = [i for i in range(text_length) if text[i] == ' ']
    
    # return index of space that is closest to the center of the string
    return min(spaces_indices, key=lambda index: abs(text_length / 2 - index))

def title_splitter(title: text_object.TextObject, title_1 : text_object.TextObject, title_2 : text_object.TextObject):

    if ' ' not in title.content:
        # if there's no space in the title, return False and the original title objects
        return False
    else:
        split_flag = False #random.choice([True, False])
        
        if not split_flag:
            # if split flag is False, return False and the original title objects
            return False
        else:
            # split the title content at the most centered space
            split_index = get_most_centered_space_index(title.content)
            title_1.content, title_2.content = title.content[:split_index], title.content[split_index+1:]

            return True
        

def layout_selector( splitter : bool) -> int : 
    if splitter == True : 
        return random.randint(4,6)
    elif splitter == False : 
        return random.randint(1,3)


background = background_object.BackgroundObject(
    color = None,
    width = 400,
    height = 300
)

title = text_object.TextObject(
    content="",
    font_size= None,
    font = None,
    x = 0,
    y = 0,
    font_color= None,
    text_font_data_encoded= None,
    scale_factor= None,
    width = 0,
    group_x = 0,
    group_y = 0
)

title_1 = text_object.TextObject(
    content="",
    font_size= None,
    font = None,
    x = 0,
    y = 0,
    font_color= None,
    text_font_data_encoded= None,
    scale_factor= None,
    width = 0,
    group_x = 0,
    group_y = 0
)

title_2 = text_object.TextObject(
    content="",
    font_size= None,
    font = None,
    x = 0,
    y = 0,
    font_color= None,
    text_font_data_encoded= None,
    scale_factor= None,
    width = 0,
    group_x = 0,
    group_y = 0
)

slogan = text_object.TextObject(
    content="",
    font_size= None,
    font = None,
    x = 0,
    y = 0,
    font_color = None,
    text_font_data_encoded= None,
    scale_factor= None,
    width = 0,
    group_x= 0,
    group_y= 0
    
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
    color = None,
    x = 0,
    y = 0,
    width = 0,
    height = 0,
    keyword = None,
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

def get_data_for_print():
    return data


def iterator( number : int , directory : Path) : 

    title.content = data["company_name"]
    slogan.content = data["slogan"] 


# extract the values of chatGPT's response 
    for i in range(number) :
 
        random.seed(i)
        random_font_size = random .randint(0,10)
        #random_vector = np.random.normal(scale=0.1, size = 6)
        #random_layout = random.randint(0,1000000)

        design_number = i + 1
        layout_number = i + 1

    #initialize the values of the rest of the parameters 
        background.color = data["design_" + str(design_number)]["color_palette"]["background_color"]
        title.font_color = data["design_" + str(design_number)]["color_palette"]["font_color"]
        slogan.font_color = data["design_" + str(design_number)]["color_palette"]["font_color"]
        center_icon.color = data["design_" + str(design_number)]["color_palette"]["icon_color"]
        center_icon.color = center_icon.color[1:]
        vector = list(data["design_" + str(design_number)]["font_vector"].values())
        #title.font = sel.find_nearest_font(np.array(list(data["design_" + str(design_number)]["font_vector"].values())), random_vector)
        title.font = sel.find_nearest_font(np.array(list(vector)[1:]))
        slogan.font = title.font
        title.text_font_data_encoded = get_font_file(title)
        slogan.text_font_data_encoded = get_font_file(slogan)
        center_icon.keyword = data["design_" + str((i%2) + 1)]["icon"]
        center_icon.png_base64 = get_png_base64(center_icon.keyword, center_icon.color, i, 7)

        # Is th title splitted?
        split = title_splitter(title, title_1, title_2)
        print(split)

        #Choose the layout
        layout_number = layout_selector(split)
        print(layout_number)
        # Apply the layout 
        tab = apply_layout(background, title, slogan,center_icon, layout_number, title_1, title_2)

        #generate the svg
        svg = generate_svg(background, title, slogan, container_icon, center_icon, letter_icon, split, title_1, title_2, tab)    
        title.font = None
        slogan.font = None

        title.x = title_1.x = title_2.x = slogan.x = 0
        title.y = title_1.y = title_2.y = slogan.y = 0
        title.width = title_1.width = title_2.width = slogan.width = 0
    
        #Create or overwrite the svg in a .svg file 
        with open(Path(str(directory) + "/" + str(i) + "_output_svg.svg"), 'w') as f:
            f.write(svg)
    
    