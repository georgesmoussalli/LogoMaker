import base64
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import get_font_file
from text_object import TextObject
from io import BytesIO

def letter_to_svg_path(letter, text : TextObject):
    # Load the font file from the binary data
    font = TTFont(BytesIO(text.text_font_data_encoded))

    # Get the glyph set
    glyph_set = font.getGlyphSet()

    # Get the Unicode code point for this letter
    unicode_code_point = ord(letter)

    # Get the glyph name for this Unicode code point
    glyph_name = font.getBestCmap().get(unicode_code_point)

    if glyph_name is None:
        # Handle the case where the glyph is not found in the font
        # You may want to log or raise an error here, or use a default glyph
        glyph_name = '.notdef'

    # Create a new pen to generate the SVG path
    pen = SVGPathPen(glyph_set)

    # Draw the glyph with the pen
    glyph_set[glyph_name].draw(pen)

    glyph_width = glyph_set[glyph_name].width

    # Get the SVG path commands
    svg_path = pen.getCommands()

    # Format the SVG path element with the letter style
    svg_path_element = f"""<path letter="{letter}" style="font-size:{text.font_size}px; font-family:'{text.font}';" d="{svg_path}" fill="{text.font_color}" transform=" translate({text.x}, {text.y}) scale({text.scale_factor}) scale(1, -1) "></path>"""
    text.x += glyph_width * text.scale_factor
    text.width += glyph_width * text.scale_factor
    return svg_path_element

def string_to_svg_paths(text : TextObject):
    # Decode the base64 font data to binary data
    text.text_font_data_encoded = base64.b64decode(text.text_font_data_encoded)

    svg_paths = []
    for letter in text.content:
        svg_path_element = letter_to_svg_path(letter, text)
        svg_paths.append(svg_path_element)

    return ''.join(svg_paths)




