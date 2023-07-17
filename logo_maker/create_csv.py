import os
import csv
from pathlib import Path

def create_csv_file(svg_list : list, folder_path : Path, input_parameters):
    # Define the CSV file pathgit 
    csv_file_path = os.path.join(folder_path, "output.csv")

    # Open the CSV file in write mode
    with open(csv_file_path, 'w', newline='') as f:
        # Create a CSV writer
        writer = csv.writer(f)
        
        # Write the header row
        writer.writerow(input_parameters)
