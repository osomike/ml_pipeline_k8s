import json

def load_json_file(json_path):
    with open(json_path) as f:
        data = json.load(f)
    
    return data