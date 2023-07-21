from app_init import initialize_app
from flask import Flask, send_from_directory

_DIR_OUTPUTS = initialize_app()
#_DIR_OUTPUTS = The output file you want to see, hardcoded to open the last one but can be changed manually 

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_from_directory(str(_DIR_OUTPUTS), 'output.html')

if __name__ == '__main__':
    app.run(port=8000)
