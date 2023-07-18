import os
from pathlib import Path

# does it work on other machines?
def get_svg_files(folder_path : Path) -> list : 
    svg_list = []
    for filename in os.listdir(folder_path) : 
        svg_list.append(os.path.join(folder_path,filename))
    return svg_list

def create_html_file(folder_path: Path) -> None:
    
    svg_list = get_svg_files(folder_path)
    # Open the HTML file in write mode
    with open(os.path.join(folder_path.parent, "output.html"), 'w') as f:
        # Write the HTML header
        f.write("<html>\n<head>\n<title>Generated SVGs</title>\n</head>\n<body>\n")
        
        # Calculate the height for each row
        row_height = "50vh"
        
        # Write the CSS style for the SVG containers
        f.write("<style>\n")
        f.write(".svg-container {\n")
        f.write("    display: inline-block;\n")
        f.write("    width: auto;\n")
        f.write("    height: 100%;\n")
        f.write("    box-sizing: border-box;\n")
        f.write("    padding: 10px;\n")
        f.write("}\n")
        f.write(".row {\n")
        f.write(f"    height: {row_height};\n")
        f.write(f"    white-space: nowrap;\n")
        f.write("}\n")
        f.write("</style>\n")
        
        # Write the upper row of SVGs
        f.write("<div class='row'>\n")
        for i in range(5):
            svg_content = open(svg_list[i]).read()
            f.write(f"<div class='svg-container'>{svg_content}</div>\n")
        f.write("</div>\n")
        
        # Write the lower row of SVGs
        f.write("<div class='row'>\n")
        for i in range(5, len(svg_list)):
            svg_content = open(svg_list[i]).read()
            f.write(f"<div class='svg-container'>{svg_content}</div>\n")
        f.write("</div>\n")
        
        # Write the HTML footer
        f.write("</body>\n</html>")
