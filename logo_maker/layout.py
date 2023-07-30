from background_object import BackgroundObject
from icon_object import IconObject
from text_object import TextObject

# Add multiple layouts!! a lot and also think about the icon placement in the text zone

def vertical_space_text(y, font_size, max_height):
    return y +  150 * font_size / max_height

def vertical_space_icon_to_text(y, font_size, max_height):
    return y +  100 * font_size / max_height

# add other layout with icon in the middle or instead of a letter or in the background or add a form in the background
def apply_layout(background : BackgroundObject, title : TextObject , slogan : TextObject, icon : IconObject, layout : int,) -> int : 
    if layout == 1 :
     
        title.x = 50
        slogan.x = 50
        #slogan.font_size = title.font_size / 2.5
        title.y = 50 + 50 * ((title.font_size - (title.font_size / 2))/background.height)
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)
        title.anchor = "middle"
        slogan.anchor = "middle"
        return 1

    elif layout == 2 : 
        icon.x = 50 - icon.width/2
        icon.y = 50 - icon.height
        title.x = 50
        slogan.x = 50
        title.y = vertical_space_icon_to_text(icon.y, title.font_size, background.height) + icon.height
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)    
        title.anchor = "middle"
        slogan.anchor = "middle"
        return 2
    
    elif layout == 3 : 
        icon.x = 50 -  icon.width * 3/2
        icon.y = 50 - icon.height/2
        title.x = icon.x + icon.width
        slogan.x = title.x 
        title.y = 50 + 50 * ((title.font_size - (title.font_size / 2))/background.height)
        slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)    
        title.anchor = "start"
        slogan.anchor = "start" 
        return 2