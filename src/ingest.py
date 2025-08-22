import json

def load_biosignal_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data
