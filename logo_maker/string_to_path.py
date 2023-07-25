import base64
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from io import BytesIO
from text_object import TextObject

def string_to_path(text : TextObject):
   # Decode the base64 font data to binary data
    font_data = base64.b64decode(text.text_font_data_encoded)

    # Load the font file from the binary data
    font = TTFont(BytesIO(font_data))

    # Get the glyph set
    glyph_set = font.getGlyphSet()

    svg_paths = ""
    for index, letter in enumerate(text.content):
        # Get the glyph name for this letter
        glyph_name = font.getGlyphID(letter)

        # Create a new pen to generate the SVG path
        pen = SVGPathPen(glyph_set)

        # Draw the glyph with the pen
        glyph_set[glyph_name].draw(pen)

        # Get the SVG path commands
        svg_path = pen.getCommands()

        # Format the SVG path element
        svg_path_element = f"""<path style="font-style:{text.font_style};font-size:{text.font_size};line-height:{text.line_height};font-family:'{text.font}';text-align:{text.align};text-anchor:{text.anchor}" d="{svg_path}" fill="#4ed0fb" transform="{text.transform}"></path>"""

        # Add this path to the overall string
        svg_paths += svg_path_element

    return svg_paths
