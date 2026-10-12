import json
from pathlib import Path
import random
from tokenize import group

# This finds the "data" folder relative to THIS file,
# so it works no matter where you run the script from.
DATA_DIR = Path(__file__).parent / "data"

def load_json(filename):
    """Load data from the JSON file."""
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)

# Load once at import
_surnames_data = load_json("surnames.json")

# Cache group files as they're loaded, so we don't re-read the disk every call
_group_cache: dict[str, dict] = {}

def _load_group(group: str) -> dict:
    if group not in _group_cache:
        _group_cache[group] = load_json(f"names_{group}.json")
    return _group_cache[group]

def _pick(entry: dict, script: str) -> str:
    """entry is {"en": "...", "np": "..."}; script is 'en' or 'np'."""
    return entry[script]


def random_first_name(group: str, gender: str, script: str = "en") -> str:
    """Return a random first name from the first_names.json file."""
    group_data = _load_group(group)
    entry = random.choice(group_data[gender])
    return _pick(entry, script)

def random_middle_name(group: str, script: str = "en") -> str:
    """Return a random middle name from the middle_names.json file."""
    group_data = _load_group(group)
    return _pick(random.choice(group_data["middle_names"]), script)

def random_surname(group: str, gender: str = "male_surnames", script: str = "en") -> str:
    """Return a random surname from the surnames.json file."""
    key = gender
    return _pick(random.choice(_surnames_data[group][key]), script)

def generate_name(group: str, gender: str = "male",
                  middle: bool = False, script: str = "en") -> str:
    """Generate a random name based on the group and gender."""
    parts = [random_first_name(group, gender, script)]
    if middle:
        parts.append(random_middle_name(group, script))
    parts.append(random_surname(group, script=script))

    return " ".join(parts)

# import json → Python's built-in tool for reading/writing JSON
# from pathlib import Path → a clean way to build file paths that works on Windows, Mac, and Linux alike
# Path(__file__).parent → "the folder this names.py file lives in" — so DATA_DIR always points to nepafaker_pkg/data, regardless of where you run the program from
# open(..., encoding="utf-8") → important — without utf-8, the Devanagari (Nepali script) text can get garbled or crash on some systems
# json.load(f) → converts the JSON file's text into a Python dictionary you can work with