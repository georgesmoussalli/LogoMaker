import os
from pathlib import Path

def create_html_file(svg_list: list, folder_path: Path) -> None:
    # Open the HTML file in write mode
    with open(os.path.join(folder_path, "output.html"), 'w') as f:
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
            f.write(f"<div class='svg-container'>{svg_list[i]}</div>\n")
        f.write("</div>\n")
        
        # Write the lower row of SVGs
        f.write("<div class='row'>\n")
        for i in range(5, len(svg_list)):
            f.write(f"<div class='svg-container'>{svg_list[i]}</div>\n")
        f.write("</div>\n")
        
        # Write the HTML footer
        f.write("</body>\n</html>")
