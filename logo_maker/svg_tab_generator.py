import background_object
from datetime import datetime
import generator
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


#import random

#random.seed(0)
number = 10
number_possible_layouts = 3
icon_number = 3
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

data = get_gpt.get_parameters()
print(data)


background = background_object.BackgroundObject(
    color = None,
    width = 400,
    height = 300
)

title = text_object.TextObject(
    content = "",
    font_size = 35,
    font_color = None,
    font = None,
    x = -100000,
    y = -100000,
    anchor = None,
    text_font_data_encoded= None
)

slogan = generator.TextObject(
    content = "",
    font_size = 14,
    font_color = None,
    font = None,
    x = -100000,
    y = -100000,
    anchor= None,
    text_font_data_encoded= None

)

icon = icon_object.IconObject(
    color = None,
    x = -100000,
    y = -100000,
    width = 20,
    height = 20,
    keyword = None,
    png_base64 = None
)

        

def get_data_for_print():
    return data


def iterator( number : int , directory : Path) : 

    title.content = data["company_name"]
    slogan.content = data["slogan"] 
    j = 0 


# extract the values of chatGPT's response 
    for i in range(number) :
 
        #random.seed(i)
        #random_vector = np.random.normal(scale=0.1, size = 6)
        #random_layout = random.randint(0,1000000)

        design_number = ( i % 5 )+ 1


    #initialize the values of the rest of the parameters 
        background.color = data["design_" + str(design_number)]["color_palette"]["background_color"]
        title.font_color = data["design_" + str(design_number)]["color_palette"]["font_color"]
        slogan.font_color = data["design_" + str(design_number)]["color_palette"]["font_color"]
        icon.color = data["design_" + str(design_number)]["color_palette"]["icon_color"]
        icon.color = icon.color[1:]
        #title.font = sel.find_nearest_font(np.array(list(data["design_" + str(design_number)]["font_vector"].values())), random_vector)
        title.font = sel.find_nearest_font(np.array(list(data["design_" + str(design_number)]["font_vector"].values())))
        slogan.font = title.font
        get_font_file(title, slogan)

        #layout_number = sel.layout_selector(number_possible_layouts, random_layout) + 1
        layout_number = (i % number_possible_layouts) + 1

        # Apply the layout 
        template = apply_layout(background, title, slogan, icon, layout_number)
        if(template == 2) : 
            icon.keyword = data["design_" + str((j%5) + 1)]["icon_keyword"]
            print(icon.keyword)
            icon.png_base64 = get_png_base64(icon.keyword, icon.color, (i % icon_number))
            j+=1


        #generate the svg
        svg = generator.generate_svg(background, title, slogan, icon, layout_number, template)   
        
        title.font = None
        slogan.font = None

        #append to the list of svg we will try to visualize in html later

        #Create or overwrite the svg in a .svg file 
        with open(Path(str(directory) + "/" + str(i) + "_output_svg.svg"), 'w') as f:
            f.write(svg)
    