# templates_registry/fields.py

def text_field(name, label):
    return {
        "name": name,
        "label": label,
        "type": "text"
    }

def combo_field(name, label, options):
    return {
        "name": name,
        "label": label,
        "type": "combo",
        "options": options
    }

def date_field(name, label):
    return {
        "name": name,
        "label": label,
        "type": "date"
    }

TIME_RANGES = [
    "7am a 9am",
    "9am a 11am",
    "11am a 1pm",
    "2pm a 4pm",
    "4pm a 6pm",
    "6pm a 8pm",
]

def time_range_field(name, label):
    return {
        "name": name,
        "label": label,
        "type": "combo",
        "options": TIME_RANGES
    }
