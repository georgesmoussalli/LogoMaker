import os
import json
from pathlib import Path
import get_gpt

def create_json_file(folder_path : Path, data):
    json_file_path = os.path.join(folder_path, "output.json")

    # Convert the Python dictionary to a JSON string
    data['prompt'] = get_gpt.get_GPT_prompt()
    data['model'] = get_gpt.get_model()
 
    json_str = json.dumps(data, indent=4)

    # Save the JSON string to a file
    with open(json_file_path, "w") as file:
        file.write(json_str)

