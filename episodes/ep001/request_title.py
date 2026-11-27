def normalize_title(text: str) -> str:
    """Return the trimmed request title, raising ValueError for a blank title."""
    textNew = text.strip()
    if len(textNew) == 0:
        raise ValueError("can not empty")
    return textNew
