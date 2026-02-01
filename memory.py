import json
import os
import config



MEMORY_FILE = "memory.json"

def _load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def _save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def remember(key, value):
    """Save a fact into memory.json"""
    data = _load_memory()
    data[key] = value
    _save_memory(data)

def recall(key):
    """Retrieve a fact from memory.json"""
    data = _load_memory()
    return data.get(key)

def forget(key):
    """Remove a fact from memory.json"""
    data = _load_memory()
    if key in data:
        del data[key]
        _save_memory(data)
        return True
    return False
def recall_all():
    """Return all stored facts from memory.json"""
    data = _load_memory()
    return data
