import json
import numpy as np
import os
from pathlib import Path

# Get the path to the data folder 
_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

# Calculate euclidian distance between two vectors
def euclidean_distance(vector1 : np.array, vector2 : np.array) -> np.array:
    return np.linalg.norm(vector1 - vector2)

# Calculate manhattan distance between two vectors
def manhattan_distance(vector1 : np.array, vector2 : np.array) -> np.array:
    return np.sum(np.abs(vector1 - vector2))

# find the name of the neareast font in input with noise 
def find_nearest_font(input_vector : np.array, random_seed : int) -> str: 
    # Load the font catalog from JSON file
    with open(str(_DIR_DATA) + '/MVPfonts.json', 'r') as file:
        catalog = json.load(file)
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    # Convert font data to 2D array
    font_data_array = np.array([[font['era'], font['maturity'], font['weight'], font['personality'], font['definition'], font['concept']]
                            for font in catalog])

    # Compute standard deviation of each feature
    std_devs = np.std(font_data_array, axis=0)
    print(std_devs)

    # Add noise to input vector
    noise = np.random.normal(scale=0.1, size = input_vector.shape) * 2 * std_devs
    input_vector = input_vector + noise
    min_distance = float('inf')
    nearest_font = ''

    for font in catalog:


        try:
            font_vector = np.array([font['era'], font['maturity'], font['weight'], font['personality'], font['definition'], font['concept']])
            distance = euclidean_distance(input_vector, font_vector)# or manhattan_distance(input_vector, font_vector)
            if distance < min_distance:
                min_distance = distance
                nearest_font = font['name']
        # Exception handling in case a font's vector doesn't have all the keys necessary for crreating a vector of parameters
        except KeyError as e:
            missing_key = e.args[0]  # Get the missing key from the exception arguments
            print(f"Skipping font {font['name']} due to missing key.")

    return nearest_font
