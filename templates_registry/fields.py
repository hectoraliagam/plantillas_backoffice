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
    "07:00 AM – 09:00 AM",
    "09:00 AM – 11:00 AM",
    "11:00 AM – 01:00 PM",
    "02:00 PM – 04:00 PM",
    "04:00 PM – 06:00 PM",
    "06:00 PM – 08:00 PM",
]

def time_range_field(name, label):
    return {
        "name": name,
        "label": label,
        "type": "combo",
        "options": TIME_RANGES
    }
