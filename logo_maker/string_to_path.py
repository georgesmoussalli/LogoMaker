import base64
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from io import BytesIO
from text_object import TextObject

def letter_to_svg_path(letter, font_data, font_style, font_size, font_family, align, anchor, letter_spacing):

    # Load the font file from the binary data
    font = TTFont(BytesIO(font_data))

    # Get the glyph set
    glyph_set = font.getGlyphSet()

    # Get the glyph name for this letter
    glyph_name = font.getGlyphID(letter)

    # Create a new pen to generate the SVG path
    pen = SVGPathPen(glyph_set)

    # Draw the glyph with the pen
    glyph_set[glyph_name].draw(pen)

    # Get the SVG path commands
    svg_path = pen.getCommands()

    # Calculate the letter spacing translation
    x_offset = len(svg_path.split('M')[1].split(' ')[0]) if 'M' in svg_path else 0
    letter_transform = f"translate({letter_spacing * x_offset}, 0)"

    # Format the SVG path element with the letter spacing translation
    svg_path_element = f"""<path style="font-style:{font_style};font-size:{font_size};font-family:'{font_family}';text-align:{align};text-anchor:{anchor}" d="{svg_path}" fill="#4ed0fb" transform="{letter_transform}"></path>"""

    return svg_path_element


def string_to_svg_paths(text: TextObject):
    # Decode the base64 font data to binary data
    font_data = base64.b64decode(text.text_font_data_encoded)

    svg_paths = []
    for letter in text.content:
        svg_path_element = letter_to_svg_path(letter, font_data, text.font_style, text.font_size, text.font, text.align, text.anchor, text.transform)
        svg_paths.append(svg_path_element)

    return ''.join(svg_paths)
