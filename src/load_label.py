import json

# Read label names from JSON file
def load_labels(label_file):
    with open(label_file, 'r') as file:
        labels = json.load(file)
    return labels