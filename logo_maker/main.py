from datetime import datetime
import font_selector as fs
import generator
import get_gpt
import numpy as np
import os
from pathlib import Path

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
number = 10 
data = get_gpt.get_parameters()
print(data)

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

def main( number : str , random_seed : int) -> list : 

    svg_tab = [] 

# extract the values of chatGPT's response 
    for i in range(number) :
        if(i < number /2 ) : 
            layout_number = 1
        else : 
            layout_number = 2
        
        design_number = ( i % 5 )+ 1


    #initialize the values of the rest of the parameters 
        background.color = data["design_" + str(design_number)]["color_palette"]["background_color"]
        title.font_color = data["design_" + str(design_number)]["color_palette"]["font_color"]
        slogan.font_color = data["design_" + str(design_number)]["color_palette"]["font_color"]
        title.font = fs.find_nearest_font(np.array(list(data["design_" + str(design_number)]["font_vector"].values())), random_seed)
        slogan.font = title.font


        #generate the svg
        svg = generator.generate_svg(background, title, slogan, icon, layout_number)


        #append to the list of svg we will try to visualize in html later
        svg_tab.append(svg)

        #Create or overwrite the svg in a .svg file 
        #with open(str(_DIR_DATA) + "/svgoutputs/" + str(i) + "svg_output.svg", 'w') as f:
            #f.write(svg)


        #Change the random seed
        random_seed += 1
    
    return svg_tab

