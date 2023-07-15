import json

import json

def find_icon_by_keyword(keyword, filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    for element in data:
        if 'keyword1' in element and element['keyword1'] == keyword:
            return "/Users/georges/Desktop/projet/icons/" + element['name']
    return None

