class IconObject:
    def __init__(self, color, x, y, width, height, keyword, png_base64, translate, scale, show : bool):

        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.keyword = keyword
        self.png_base64 = png_base64
        self.translate = translate 
        self.scale = scale