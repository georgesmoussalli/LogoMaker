import base64
import csv
from datetime import datetime
import FontSelectorMVP as FS
import IconSelectorMVP as IS
import numpy as np
import LayoutSelectorMVP as LS
import openai 
import json

openai.api_key = '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'

user_prompt = "My company is a huge VC company called \" Really Ventures\" handling portfolios for very wealthy and old money clients who want to invest for a great return but lots of risk. My business is already huge."
prompt_for_GPT = "Put yourself in a situation where a user writes a prompt describing his business/ company and find the 5 most appropriate color palettes composed of a background color, a font color and an icon color to generate a logo for the company/business of the user. If some color or adjectives are mentioned  by the user ChatGPT4 should take this into account but for example if blue is said in the prompt and you want to take it into account but not always literally. You can but you can also add a nuanced blue and not blue as a primary color. If not It should understand in what industry the user's company is in and what adjective describes his business the best to find the 5 most suited color palette. Determine the name of the company and enter it in all caps in the output.Also if the user enters a slogan, stock it in the dictinnary, if not just store an empty string .Also determine one input vector and make it appear only once in the json output composed of these parameters where the values where entered for example purposes  \"input_vector_font\" : {\"era\": 0.5, \"maturity\": 0.7, \"weight\": 0.7, \"personality\": 0.5, \"definition\": 0.2, \"concept\": 0.5} Choose the values in function of what seems more appropriate in terms of font to describe the users business. Each parameter is between 0 and 1. Era : does the font look traditional (0) or modern (1.0) ; Maturity : does the font look mature(0) or youthful (1.0); Weight : does the font look thin (0) or bold (1.0); Personality : does the font look playful (0) or sophisticated (1.0); Definition : does the font look organic (0) or geometric (1.0); Concept : does the font look abstract (0) or literal (1.0) Input : " + user_prompt + " Output : 3 best suited color palettes in the best suited way and best suited input vector for the font in this format :chatGPT_inputs = [{\"background_color\":\"color in hex\", \"font_color\":\"color in hex\", \"icon_color\" : \"color in hex\"},  {\"background_color\":\"color in hex\", \"font_color\":\"color in hex\", \"icon_color\" : \"color in hex\"},  {\"background_color\":\"color in hex\", \"font_color\":\"color in hex\", \"icon_color\" : \"color in hex\"},{\"background_color\":\"color in hex\", \"font_color\":\"color in hex\", \"icon_color\" : \"color in hex\"},{\"background_color\":\"color in hex\", \"font_color\":\"color in hex\", \"icon_color\" : \"color in hex\"},{\"slogan\" : \"Example\"}, {\"company_name\" : \"Example\"}, {\"input_vector_font\" : \"(Example)\"}]"
kewyord = "moon" #input("Please enter your keyword: ")
number = 10
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
API = "GPT3"



template_code = """
<svg xmlns='http://www.w3.org/2000/svg' width='{background.width}' height='{background.height}'>
    <style>
        @font-face {{
            font-family: '{title.font}';
            src: url(data:font/ttf;base64,{title_font_data}) format('truetype');
        }}
        @font-face {{
            font-family: '{slogan.font}';
            src: url(data:font/ttf;base64,{slogan_font_data}) format('truetype');
        }}
    </style>
    <rect width='100%' height='100%' fill='{background.color}' />
    <text x='{title.x}%' y='{title.y}%' text-anchor='{title.anchor}' font-size='{title.font_size}' font-family='{title.font}' fill='{title.font_color}'>{title.content}</text>
    <text x='50%' y='{slogan.y}%' text-anchor='{slogan.anchor}' font-size='{slogan.font_size}' font-family='{slogan.font}' fill='{slogan.font_color}'>{slogan.content}</text>
    <image href='{icon}' x='{icon.x}%' y='{icon.y}%' width='{icon.width}%' height='{icon.height}%' />
</svg>
"""
html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-content: space-around;
}
</style>
</head>
<body>
{svg_content}
</body>
</html>
"""


svg_content_all = ''
parameters = []


class LayoutHelper:
    def __init__(self, layout, texts, icon):
        self.layout = layout
        self.texts = texts
        self.icon = icon

    def apply_layout(self):
        if self.layout == 1:
            self._apply_layout1()
        elif self.layout == 2:
            self._apply_layout2()
        #other layouts
        else: print("Error: no layout chosen")

    def _apply_layout1(self):
       title.x = 50
       slogan.x = 50
       #slogan.font_size = title.font_size / 2.5
       title.y = 50 + 50 * ((title.font_size - (title.font_size / 2))/background.height)
       slogan.y = vertical_space(title.y, slogan.font_size, background.height)
       
    def _apply_layout2(self):   
       icon.x = 50 - icon.width/2
       icon.y = 50 - icon.height
       title.x = 50
       slogan.x = 50
       title.y = vertical_space(icon.y, title.font_size, background.height) + icon.height
       slogan.y = vertical_space(title.y, slogan.font_size, background.height)


class TextObject:
    def __init__(self, content, font_size, font_color, font, x, y, anchor):
        self.content = content
        self.font_size = font_size
        self.font_color = font_color
        self.font = font
        self.x = x
        self.y = y
        self.anchor = anchor

class IconObject:
    def __init__(self, file_path, x, y, width, height):
        self.file_path = file_path 
        self.data_uri = "None"
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def _generate_data_uri(self):
        with open(self.file_path, "rb") as f:
            icon_data = f.read()
        icon_data_uri = "data:image/svg+xml;base64," + base64.b64encode(icon_data).decode("utf-8")
        return icon_data_uri
    
    def __str__(self):
        return self.data_uri

    
class BackgroundObject:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def __str__(self):
        return self.color
    


def vertical_space(y, font_size, max_height):
    return y + 50 * 1.85 * font_size / max_height

def splitter(brand_name, title, title2):
    length = len(brand_name)
    middle_index = length // 2

    for i in range(middle_index, -1, -1):
        if brand_name[i] == ' ':
            title.content = brand_name[:i]
            title2.content = brand_name[i+1:]
            return True
            
    else:
        title.content = brand_name
        title2.content = ""
        return False
    
def get_chatGPT_inputs(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=3000
    )
    print(response)
    # Parse the output from the model to get the color palettes and font vector
    output_lines = response.choices[0].text.strip().split('\n')
    chatGPT_output = []

    for line in output_lines:
        if line.startswith("chatGPT_output =") or line.startswith("chatGPT_inputs ="):
            # Extract the JSON string from the line
            json_str = line.split(" = ")[1].strip()
            # Parse the JSON string as a list of dictionaries
            input_data = json.loads(json_str)
            chatGPT_output.extend(input_data)

    print(chatGPT_output)
    return chatGPT_output

def generate_svg(background, title, slogan, icon, layoutHelper):
    
    #Check if title is 2 words
    #boolean = splitter(brand_name, title, title2)

    #Chose and apply layout
    #layoutHelper.layout = LS.choose_layout()
    if(icon.file_path == None):
        layoutHelper.layout = 1
    else:
        icon.data_uri = icon._generate_data_uri()
        layoutHelper.layout = 2
    layoutHelper.apply_layout()

     # Read the font files as binary data
    font_formats = [".otf", ".ttf"]
    title_font_data = None
    slogan_font_data = None

    for font_format in font_formats:
        try:
            with open("/Users/georges/Desktop/projet/fonts/" + title.font + font_format, "rb") as title_font_file:
                title_font_data = title_font_file.read()
            with open("/Users/georges/Desktop/projet/fonts/" + slogan.font + font_format, "rb") as slogan_font_file:
                slogan_font_data = slogan_font_file.read()
            break  # If opening the font files succeeds, exit the loop
        except FileNotFoundError:
            continue  # If font files are not found, try the next format

    if title_font_data is None or slogan_font_data is None:
        raise FileNotFoundError("Font files not found for title or slogan.")

    # Encode the font data in base64
    title_font_data_encoded = base64.b64encode(title_font_data).decode("utf-8")
    slogan_font_data_encoded = base64.b64encode(slogan_font_data).decode("utf-8")

    # Inject the font data into the SVG template
    svg_content = template_code.format(
        background=background,
        title=title,
        slogan=slogan,
        icon=icon,
        title_font_data=title_font_data_encoded,
        slogan_font_data=slogan_font_data_encoded
    )


    return svg_content



background = BackgroundObject(
    color = None,
    width = 400,
    height = 300
)

title = TextObject(
    content = "",
    font_size = 40,
    font_color = None,
    font = None,
    x = -100000,
    y = -100000,
    anchor = "middle"# change that it the template and determine it it the layout
)

#title2 = TextObject(
    #content = None,
    #font_size = 50,
    #font_color = "#318CE7",
    #font = FS.find_nearest_font(input_vector_font_1, random_seed),
    #x = 0,
    #y = 0,
    #anchor="middle"
#)

slogan = TextObject(
    content = "",
    font_size = 14,
    font_color = None,
    font = None,
    x = -100000,
    y = -100000,
    anchor="middle" # change that it the template and determine it it the layout

)

icon = IconObject(
    file_path= None,
    x = -100000,
    y = -100000,
    width = 20,
    height = 20
)

layoutHelper = LayoutHelper(
    layout = None,
    texts = [title, slogan],
    icon = icon
)  



background_colors = []
font_colors = []
icon_colors = []


chatGPT_inputs = get_chatGPT_inputs(prompt_for_GPT)
print(chatGPT_inputs)

for input_data in chatGPT_inputs:
    if 'background_color' in input_data:
        background_colors.append(input_data['background_color'])
    if 'font_color' in input_data:
        font_colors.append(input_data['font_color'])
    if 'icon_color' in input_data:
        icon_colors.append(input_data['icon_color'])

input_slogan_dict = chatGPT_inputs[-3] # get the third to last dictionary's 'slogan'
if input_slogan_dict:
    # Extract the values from the dictionary and convert to a numpy array
    input_slogan_content = input_slogan_dict.get('slogan')
else:
    input_slogan_content = None

input_brand_dict = chatGPT_inputs[-2]  # get the second to last dictionary's 'company_name'
if input_brand_dict:
    # Extract the values from the dictionary and convert to a numpy array
    input_brand_content = input_brand_dict.get('company_name')


# Extract the values from the dictionary and convert to a numpy array
dict = chatGPT_inputs[-1]['input_vector_font']
input_vector_font = np.array(list(dict.values()))

random_seed =0
for i in range(number):

    title.font = FS.find_nearest_font(input_vector_font, random_seed)
    slogan.font = title.font #FS.find_nearest_font(input_vector_font_2, random_seed)
    
    background.color = background_colors[i%5]
    title.font_color =  font_colors[i%5]
    slogan.font_color = icon_colors[i%5]# a changer et rajouter 1 couleur en plus dans la palette pour l icone 
    
    title.content = input_brand_content
    slogan.content = input_slogan_content

    if(i >= number/2):
        icon.file_path = IS.find_icon_by_keyword(kewyord, "MVPicons.json")
        svg_content = generate_svg(background, title, slogan, icon, layoutHelper) 
        print(svg_content)   
        svg_content_all += f"<div>{svg_content}</div>"
        parameters.append([background.color, title.font, slogan.font, icon.file_path])

    random_seed += 1


with open(f"/users/georges/Desktop/projet/LogosOutput/Logos-{timestamp}.html", "w") as html_file:
    html_file.write(html.format(svg_content = "svg_content_all"))

with open(f"/users/georges/Desktop/projet/LogosOutput/Parameters-{timestamp}.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["background_color", "title_font", "slogan_font", "icon_file_path", "random_seed", API])  # Header
    writer.writerows(parameters)  # Data
    