from datetime import datetime
import select_random as sel
import generator
import get_gpt
import numpy as np
import os
from pathlib import Path
import random

random.seed(0)
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
number = 10 
number_possible_layouts = 2
data = get_gpt.get_parameters()

_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

background = generator.BackgroundObject(
    color = None,
    width = 400,
    height = 300
)

title = generator.TextObject(
    content = "",
    font_size = 40,
    font_color = None,
    font = None,
    x = -100000,
    y = -100000,
    anchor = None 
)

slogan = generator.TextObject(
    content = "",
    font_size = 14,
    font_color = None,
    font = None,
    x = -100000,
    y = -100000,
    anchor= None 

)

icon = generator.IconObject(
    file_path= None,
    x = -100000,
    y = -100000,
    width = 20,
    height = 20
)


# initialize the values of some parameters
title.content = data["company_name"]
slogan.content = data["slogan"]

def iterator( number : str , random_seed : int) -> list : 

    svg_tab = [] 

# extract the values of chatGPT's response 
    for i in range(number) :

        random.seed(i)
        random_vector = np.random.normal(scale=0.1, size = 6)
        random_layout = random.randint(0,1000000)

        design_number = ( i % 5 )+ 1


    #initialize the values of the rest of the parameters 
        background.color = data["design_" + str(design_number)]["color_palette"]["background_color"]
        title.font_color = data["design_" + str(design_number)]["color_palette"]["font_color"]
        slogan.font_color = data["design_" + str(design_number)]["color_palette"]["font_color"]
        title.font = sel.find_nearest_font(np.array(list(data["design_" + str(design_number)]["font_vector"].values())), random_vector)
        slogan.font = title.font
        icon.file_path = str(_DIR_DATA) + "/moon.svg"
        icon.data_uri = icon._generate_data_uri()  
        layout_number = sel.layout_selector(number_possible_layouts, random_layout) + 1
        print(layout_number)

        #generate the svg
        svg = generator.generate_svg(background, title, slogan, icon, layout_number)   
        
        title.font = None
        slogan.font = None

        #append to the list of svg we will try to visualize in html later
        svg_tab.append(svg)

        #Create or overwrite the svg in a .svg file 
        #with open(str(_DIR_DATA) + "/svgoutputs/" + str(i) + "svg_output.svg", 'w') as f:
            #f.write(svg)
    
    return svg_tab

