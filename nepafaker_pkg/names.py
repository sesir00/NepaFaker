import json
from pathlib import Path

# This finds the "data" folder relative to THIS file,
# so it works no matter where you run the script from.
DATA_DIR = Path(__file__).parent / "data"

def load_names(filename):
    """Load names from the JSON file."""
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)

def load_all_data():
    """Load every JSON file in data/ into one dictionary,
        keyed by filename (without .json)."""
    all_data = {}
    for file_path in DATA_DIR.glob("*.json"):
        key = file_path.stem  # filename without .json
        all_data[key] = load_names(file_path.name)
    return all_data



# import json → Python's built-in tool for reading/writing JSON
# from pathlib import Path → a clean way to build file paths that works on Windows, Mac, and Linux alike
# Path(__file__).parent → "the folder this names.py file lives in" — so DATA_DIR always points to nepafaker_pkg/data, regardless of where you run the program from
# open(..., encoding="utf-8") → important — without utf-8, the Devanagari (Nepali script) text can get garbled or crash on some systems
# json.load(f) → converts the JSON file's text into a Python dictionary you can work with