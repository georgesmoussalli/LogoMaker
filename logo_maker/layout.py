from background_object import BackgroundObject
from icon_object import IconObject
from text_object import TextObject


def vertical_space_text(y, font_size, max_height):
    return y +  5 * font_size

def vertical_space_icon_to_text(y, font_size, max_height):
    return y +  100 * font_size / max_height

    
def apply_layout(background : BackgroundObject, title : TextObject , slogan : TextObject, center_icon : IconObject, layout : int ) -> int : 
    if layout == 1 :

        title.anchor = "middle"
        center_icon.x= -10000
        center_icon.y = -10000
        title.center_x = 200 - 0.5 * title.width
        title.center_y = 150 + 0.125 * title.font_size

        if(slogan.content != "") :
            slogan.y = vertical_space_text(title.y, slogan.font_size, background.height)
            print(slogan.y)
            print(title.y)
            slogan.anchor = "middle"
    
        return 1    

    elif layout == 2 : 
        title.width = 250
        slogan.width = 250
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