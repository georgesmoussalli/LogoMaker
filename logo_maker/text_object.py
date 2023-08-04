class TextObject:
    def __init__(self, content, font_size, font_color, font, x, y, text_font_data_encoded, anchor, scale_factor , width, center_x , center_y ) :
        self.content = content
        self.font_size = font_size
        self.font_color = font_color
        self.font = font
        self.x = x
        self.y = y
        self.text_font_data_encoded = text_font_data_encoded
        self.anchor = anchor
        self.scale_factor = scale_factor
        self.width = width
        self.center_x = center_x
        self.center_y = center_y
