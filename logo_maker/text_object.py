class TextObject:
    def __init__(self, content, font_size, font_color, font, x, y, anchor, text_font_data_encoded):
        self.content = content
        self.font_size = font_size
        self.font_color = font_color
        self.font = font
        self.x = x
        self.y = y
        self.anchor = anchor
        self.text_font_data_encoded = text_font_data_encoded
