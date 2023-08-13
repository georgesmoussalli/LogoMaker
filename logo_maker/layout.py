from background_object import BackgroundObject
from icon_object import IconObject
from text_object import TextObject
from string_to_path import string_to_svg_paths
from get_font_file import get_font_file
import random


def font_size_selector( text : TextObject, background : BackgroundObject, random_size : float) -> float :
    # Calculate the initial font size based on the ratio of logo width to text length
    initial_font_size = int(background.width / len(text.content)) + random_size
    
    # Limit the font size to the specified range
    font_size = max(min(initial_font_size, 60), 10)   
    return font_size

def vertical_space_text(title : TextObject, slogan : TextObject):
    return title.group_y + 1.1 * (title.font_size + slogan.font_size) / 2

def font_size_to_scale(font_size : int, font_size_range : range, scale_range : range) -> float : 
    min_font_size, max_font_size = font_size_range
    min_scale, max_scale = scale_range

    if font_size < min_font_size:
        return min_scale
    if font_size > max_font_size:
        return max_scale

    scale = min_scale + ((font_size - min_font_size) / (max_font_size - min_font_size)) * (max_scale - min_scale)
    return scale

def icon_size_selector(background : BackgroundObject, random_size : float) -> float : 
    return background.height * 0.25 + random_size
    
def apply_layout(background : BackgroundObject, title : TextObject , slogan : TextObject, center_icon : IconObject, layout : int, title_1 : TextObject, title_2 : TextObject) -> int : 
    random.seed(1)
    random_size = random.uniform(-2.5,2.5)
    font_size_range = (10, 70)  # This means that font sizes go from 10 to 20
    scale_range = (0.015, 0.09)  # This means that scales go from 1.0 to 2.0
    title.font_size = title_1.font_size = title_2.font_size = font_size_selector(title, background, random_size)
    title.scale_factor = title_1.scale_factor = title_2.scale_factor = font_size_to_scale(title.font_size, font_size_range, scale_range)
    slogan.font_size = min(font_size_selector(slogan, background, random_size), title.font_size)
    slogan.scale_factor = font_size_to_scale(slogan.font_size, font_size_range,scale_range )
    title.text_font_data_encoded = title_1.text_font_data_encoded = title_2.text_font_data_encoded = get_font_file(title)
    slogan.text_font_data_encoded = get_font_file(slogan)

    if layout == 1 :
        tab = [None]*3
        title_paths = string_to_svg_paths(title)
        slogan_paths = string_to_svg_paths(slogan)
        center_icon.x= -10000
        center_icon.y = -10000
        title.group_x = 200 - title.width * 0.5
        title.group_y = 150 + 0.5 * title.font_size
        slogan.group_x = 200 - slogan.width * 0.5
        slogan.group_y = vertical_space_text(title, slogan)
        tab[0] = 1
        tab[1] = title_paths
        tab[2] = slogan_paths
        return tab   

    elif layout == 2 : 
        tab = [None]*3
        title_paths = string_to_svg_paths(title)
        slogan_paths = string_to_svg_paths(slogan)
        title.group_x = 200 - title.width * 0.5
        title.group_y = 150 + title.font_size
        slogan.group_x = 200 - slogan.width * 0.5
        slogan.group_y = vertical_space_text(title, slogan)
        center_icon.height = icon_size_selector(background, 2 * random_size)
        center_icon.width = center_icon.height
        center_icon.x= 200 - center_icon.width/2
        center_icon.y = 150 - 1.1 * center_icon.height
        tab[0] = 2
        tab[1] = title_paths
        tab[2] = slogan_paths
        return tab
    
    elif layout == 3 : 
        tab = [None]*3
        title_paths = string_to_svg_paths(title)
        slogan_paths = string_to_svg_paths(slogan)
        title.group_x = 130
        title.group_y = 150 
        slogan.group_x = 130
        slogan.group_y = vertical_space_text(title, slogan)
        center_icon.height = icon_size_selector(background, 2 * random_size)
        center_icon.width = center_icon.height
        center_icon.x= title.group_x - 1.2 * center_icon.width
        center_icon.y = title.group_y - 0.5 * center_icon.height
        tab[0] = 3
        tab[1] = title_paths
        tab[2] = slogan_paths
        return tab
    
    elif layout == 4 :
        tab = [None]*4
        title_1_paths = string_to_svg_paths(title_1)
        title_2_paths = string_to_svg_paths(title_2)
        slogan_paths = string_to_svg_paths(slogan)
        center_icon.x= -10000
        center_icon.y = -10000
        title_1.group_x =  200 - title_1.width * 0.5
        title_2.group_x = 200 - title_2.width * 0.5
        title_1.group_y = 150 
        title_2.group_y = vertical_space_text(title_1, title_2)
        slogan.group_x = 200 - slogan.width * 0.5
        slogan.group_y = vertical_space_text(title_2, slogan)
        tab[0] = 4
        tab[1] = title_1_paths
        tab[2] = title_2_paths
        tab[3] = slogan_paths
        return tab
    
    elif layout == 5 : 
        tab = [None]*4
        title_1_paths = string_to_svg_paths(title_1)
        title_2_paths = string_to_svg_paths(title_2)
        slogan_paths = string_to_svg_paths(slogan)
        title_1.group_x =  200 - title_1.width * 0.5
        title_2.group_x = 200 - title_2.width * 0.5
        title_1.group_y = 150 + 0.5 * title_1.font_size
        title_2.group_y = vertical_space_text(title_1, title_2)
        slogan.group_x = 200 - slogan.width * 0.5
        slogan.group_y = vertical_space_text(title_2, slogan)
        center_icon.height = icon_size_selector(background, 2 * random_size)
        center_icon.width = center_icon.height
        center_icon.x= 200 - center_icon.width/2
        center_icon.y = title_1.group_y - 1.5 * center_icon.height
        tab[0] = 5
        tab[1] = title_1_paths
        tab[2] = title_2_paths
        tab[3] = slogan_paths
        return tab
    
    elif layout == 6 : 
        tab = [None]*4
        title_1_paths = string_to_svg_paths(title_1)
        title_2_paths = string_to_svg_paths(title_2)
        slogan_paths = string_to_svg_paths(slogan)
        center_icon.height = icon_size_selector(background, 2 * random_size)
        center_icon.width = center_icon.height
        center_icon.x= 200 - center_icon.width/2 + (title_1.width - title_2.width) * 0.5
        center_icon.y = 150 - center_icon.height/2
        title_1.group_x =  200 - title_1.width - center_icon.width / 2 + (title_1.width - title_2.width) * 0.5
        title_2.group_x = 200 + center_icon.width/2 + (title_1.width - title_2.width) * 0.5
        title_1.group_y = title_2.group_y = 150 + 0.5 * title_1.font_size
        slogan.group_x = 200 - slogan.width * 0.5
        slogan.group_y = vertical_space_text(title_2, slogan)

        tab[0] = 6
        tab[1] = title_1_paths
        tab[2] = title_2_paths
        tab[3] = slogan_paths
        return tab