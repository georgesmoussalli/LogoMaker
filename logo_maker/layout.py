from background_object import BackgroundObject
from icon_object import IconObject
from text_object import TextObject


def vertical_space_text(y, font_size, max_height):
    return y +  150 * font_size / max_height

def vertical_space_icon_to_text(y, font_size, max_height):
    return y +  100 * font_size / max_height

def font_size_selector( text : TextObject, background : BackgroundObject, random : int) -> int :
    # Calculate the initial font size based on the ratio of logo width to text length
    initial_font_size = int(background.width / len(text.content))
    
    # Limit the font size to the specified range
    font_size = max(min(initial_font_size, 70), 10)
    
    return font_size

def spacing_size_selector(text : TextObject) -> int :
    # Calculate the total width required by the text at the chosen font size
    text_width = len(text.content) * text.font_size
    
    # Calculate the remaining width for spacing
    remaining_width = text.width - text_width
    
    # Calculate the optimal spacing by distributing the remaining width evenly
    spacing = remaining_width / ( len(text.content) - 1)
    
    return spacing

def apply_layout(background : BackgroundObject, title : TextObject , slogan : TextObject, center_icon : IconObject, layout : int, random : int) -> int : 
    if layout == 1 :
        title.width = 250
        slogan.width = 250
        title.font_size = font_size_selector(title, background, random)
        slogan.font_size = min(font_size_selector(slogan, background, random), title.font_size)
        title.spacing = spacing_size_selector(title)
        slogan.spacing = spacing_size_selector(slogan)
        title.x = 50
        slogan.x = 50
        title.y = 50 + 50 * ((title.font_size - (title.font_size / 2))/background.height)
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)
        title.anchor = "middle"
        slogan.anchor = "middle"
        title.scale_factor = 0.1
        slogan.scale_factor = 0.1
        center_icon.x= -10000
        center_icon.y = -10000
        title.center_x = 50
        title.center_y = title.y
        
        return 1    

    elif layout == 2 : 
        title.width = 250
        slogan.width = 250
        title.font_size = font_size_selector(title, background, random)        
        slogan.font_size = min(font_size_selector(slogan,background, random), title.font_size)
        title.spacing = spacing_size_selector(title)
        slogan.spacing = spacing_size_selector(slogan)
        center_icon.x = 50 - center_icon.width/2
        center_icon.y = 50 - center_icon.height
        title.x = 50
        slogan.x = 50
        title.y = vertical_space_icon_to_text(center_icon.y, title.font_size, background.height) + center_icon.height
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)    
        title.anchor = "middle"
        slogan.anchor = "middle"
        title.scale_factor = 0.05
        slogan.scale_factor = 0.05
        title.center_x = 50
        title.center_y = title.y
        return 2
    
    elif layout == 3 : 
        title.width = 250
        slogan.width = 250
        title.font_size = font_size_selector(title, background, random)
        slogan.font_size = min(font_size_selector(slogan,background, random), title.font_size)
        title.spacing = spacing_size_selector(title)
        slogan.spacing = spacing_size_selector(slogan)
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