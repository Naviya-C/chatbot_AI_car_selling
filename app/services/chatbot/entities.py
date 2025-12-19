import re

def extract_budget(message: str) -> float | None:
    text = message.lower()

    pattern = "(\d+)\s*(million|k|thousand|lakh|laksha)?"

    match = re.search(pattern, text)

    if not match:
        return None
    
    value = int(match.group(1))
    unit = match.group(2)

    if unit == "million":
        value *= 1_000_000
    elif unit in ("k", "thousand"):
        value *= 1_000
    elif unit in ("lakh", "laksha"):
        value *= 100_000
    
    return value