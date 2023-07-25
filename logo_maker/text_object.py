class TextObject:
    def __init__(self, content, font_size, font_color, font, x, y, anchor, text_font_data_encoded, align , transform, font_style, line_height, spacing) :
        self.content = content
        self.font_size = font_size
        self.font_color = font_color
        self.font = font
        self.x = x
        self.y = y
        self.anchor = anchor
        self.text_font_data_encoded = text_font_data_encoded
        self.align = align
        self.transform = transform
        self.font_style = font_style
        self.line_height = line_height
        self.spacing = spacing