import create_json
import create_html
from datetime import datetime
import os 
from pathlib import Path
import svg_tab_generator


def initialize_app():
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    _HERE = Path(os.path.abspath(__file__))
    _DIR_OUTPUTS_SVG = _HERE.parent.parent.joinpath("data/outputs", timestamp, "svg")
    os.makedirs(_DIR_OUTPUTS_SVG, exist_ok= True)


    # Call the ierator function
    svg_tab_generator.iterator(6, _DIR_OUTPUTS_SVG)

    #Create the HTML file
    create_html.create_html_file(_DIR_OUTPUTS_SVG)

    #Create the JSON file
    create_json.create_json_file(_DIR_OUTPUTS_SVG.parent, svg_tab_generator.get_data_for_print())

    return _DIR_OUTPUTS_SVG.parent

