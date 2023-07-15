import numpy as np

tab = [{'input_vector_font': {'era': 0.7, 'maturity': 0.9, 'weight': 0.9, 'personality': 0.9, 'definition': 0.7, 'concept': 0.9}}]

input_vector_font = tab[0]['input_vector_font']
values_array = np.array(list(input_vector_font.values()))

print(values_array)