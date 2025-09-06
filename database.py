import json
from config import JSON_FILE_PATH

def load_database():
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_database(data):
    with open(JSON_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def find_entry_by_name(data, card_name):
    for entry in data:
        if entry.get("card_name") == card_name:
            return entry
    return None

def is_image_in_database(data, image_name):
    return any(entry.get("image_name") == image_name for entry in data)
