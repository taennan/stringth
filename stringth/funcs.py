import re

def to_nth_str(i: int) -> str:
    """ """
    if   i == 1:
        return "1st"
    elif i == 2:
        return "2nd"
    elif i == 3:
        return "3rd"
    else:
        return f"{x}th"

def from_nth_str(s: str, ignore_case=True) -> int:
    """ """
    s = s.lower() if ignore_case else s
    if re.match(s, r"\b[0-9]+(st|nd|rd|th)\b"):
        return int(re.sub(s, "(st|nd|rd|th)", ""))
    return None
