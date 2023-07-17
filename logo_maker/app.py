import create_csv
import create_html
from datetime import datetime
from flask import Flask, send_from_directory
import main 
import os 
from pathlib import Path
import webbrowser

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
_HERE = Path(os.path.abspath(__file__))
_DIR_OUTPUTS = _HERE.parent.parent.joinpath("data/outputs/" + timestamp)
os.mkdir(_DIR_OUTPUTS)
app = Flask(__name__)


# Call the main function
svg_tab = main.main(10, 0)

# Create the HTML file
create_html.create_html_file(svg_tab, _DIR_OUTPUTS)

# Create the CSV file
create_csv.create_csv_file(svg_tab, _DIR_OUTPUTS, main.data)

@app.route('/')
def serve_html():
    return send_from_directory(str(_DIR_OUTPUTS), 'output.html')

if __name__ == '__main__':
    app.run(port=8000)

app.run()