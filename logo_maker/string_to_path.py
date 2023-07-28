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

    # Get the SVG path commands
    svg_path = pen.getCommands()

    # Format the SVG path element with the letter style
    svg_path_element = f"""<path letter="{letter}" style="font-size:{text.font_size}px; font-family:'{text.font}';" d="{svg_path}" fill="{text.font_color}" transform=" translate({text.x}, {text.y}) scale({text.scale_factor}) scale(1, -1) "></path>"""
    text.x += text.spacing

    return svg_path_element

def string_to_svg_paths(text : TextObject):
    # Decode the base64 font data to binary data
    text.text_font_data_encoded = base64.b64decode(text.text_font_data_encoded)

    svg_paths = []
    for letter in text.content:
        svg_path_element = letter_to_svg_path(letter, text)
        svg_paths.append(svg_path_element)

    return ''.join(svg_paths)

slogan = TextObject(
    content="Coffee",
    font_size=40,
    font="Unique",
    x = 0,
    y = 200,
    font_color= "#E4EE3E",
    text_font_data_encoded= None,
    anchor = "",
    scale_factor= 0.1,
    align = "",
    spacing=60   
)

slogan.text_font_data_encoded = get_font_file.get_font_file(slogan)

def create_svg_document(svg_code, width, height):
    svg_template = f"""
    <svg width="{width}" height="{height}" version="1.1" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#cccccc" />
      <g id="slogan">
        {svg_code}
      </g>
    </svg>
    """
    return svg_template

svg_document = create_svg_document(string_to_svg_paths(slogan), 400, 300)
print(svg_document)




