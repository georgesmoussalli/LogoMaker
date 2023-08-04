from background_object import BackgroundObject
from icon_object import IconObject
from text_object import TextObject
from string_to_path import string_to_svg_paths
from get_font_file import get_font_file
import random


def font_size_selector( text : TextObject, background : BackgroundObject, random_size : int) -> int :
    # Calculate the initial font size based on the ratio of logo width to text length
    initial_font_size = int(background.width / len(text.content)) + random_size
    
    # Limit the font size to the specified range
    font_size = max(min(initial_font_size, 70), 10)   
    return font_size

def vertical_space_text(title : TextObject, slogan : TextObject):
    return title.group_y + (title.font_size + slogan.font_size) / 2

def font_size_to_scale(font_size : int, font_size_range : range, scale_range : range) -> float : 
    min_font_size, max_font_size = font_size_range
    min_scale, max_scale = scale_range

    if font_size < min_font_size:
        return min_scale
    if font_size > max_font_size:
        return max_scale

    scale = min_scale + ((font_size - min_font_size) / (max_font_size - min_font_size)) * (max_scale - min_scale)
    return scale


def vertical_space_icon_to_text(y, font_size, max_height):
    return y +  100 * font_size / max_height

    
def apply_layout(background : BackgroundObject, title : TextObject , slogan : TextObject, center_icon : IconObject, layout : int ) -> int : 
    random.seed(1)
    random_size = random.uniform(-2.5,2.5)
    font_size_range = (10, 70)  # This means that font sizes go from 10 to 20
    scale_range = (0.015, 0.1)  # This means that scales go from 1.0 to 2.0
    title.font_size = font_size_selector(title, background, random_size)
    title.scale_factor = font_size_to_scale(title.font_size, font_size_range, scale_range)
    slogan.font_size = min(font_size_selector(slogan, background, random_size), title.font_size)
    slogan.scale_factor = font_size_to_scale(slogan.font_size, font_size_range,scale_range )
    title.text_font_data_encoded = get_font_file(title)
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
        center_icon.x= -10000
        center_icon.y = -10000
        title.group_x = 200 - title.width * 0.5
        title.group_y = 150 + title.font_size
        slogan.group_x = 200 - slogan.width * 0.5
        slogan.group_y = vertical_space_text(title, slogan)
        tab[0] = 2
        tab[1] = title_paths
        tab[2] = slogan_paths
        return tab
    
    elif layout == 3 : 
        title.width = 250
        slogan.width = 250
        center_icon.x = 50 -  center_icon.width * 3/2
        center_icon.y = 50 - center_icon.height/2
        title.x = center_icon.x + center_icon.width
        slogan.x = title.x 
        title.y = 50 + 50 * ((title.font_size - (title.font_size / 2))/background.height)
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)    
        title.anchor = "start"
        slogan.anchor = "start"
        title.scale_factor = 0.05
        slogan.scale_factor = 0.05
        title.center_x = 50
        title.center_y = title.y
        return 2