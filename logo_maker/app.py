import create_csv
import create_html
from datetime import datetime
import main 
import os 
from pathlib import Path
import webbrowser

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
_HERE = Path(os.path.abspath(__file__))
_DIR_OUTPUTS = _HERE.parent.parent.joinpath("data/outputs/" + timestamp)
os.mkdir(_DIR_OUTPUTS)

# Call the main function
svg_tab = main.main(10, 0)

# Create the HTML file
create_html.create_html_file(svg_tab, _DIR_OUTPUTS)

# Create the CSV file
create_csv.create_csv_file(svg_tab, _DIR_OUTPUTS, main.data)

# Open the HTML file in the default web browser
html_file_path = os.path.join(_DIR_OUTPUTS / "output.html")
print(html_file_path)
webbrowser.get('safari').open(html_file_path)
