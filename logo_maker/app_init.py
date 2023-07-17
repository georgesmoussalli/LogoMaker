import create_json
import create_html
from datetime import datetime
import svg_tab_generator 
import os 
from pathlib import Path

def initialize_app():
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    _HERE = Path(os.path.abspath(__file__))
    _DIR_OUTPUTS = _HERE.parent.parent.joinpath("data/outputs/" + timestamp)
    os.mkdir(_DIR_OUTPUTS)

    # Call the ierator function
    svg_tab = svg_tab_generator.iterator(10, 0)

    # Create the HTML file
    create_html.create_html_file(svg_tab, _DIR_OUTPUTS)

    # Create the CSV file
    create_json.create_json_file(_DIR_OUTPUTS, svg_tab_generator.data)

    return _DIR_OUTPUTS
