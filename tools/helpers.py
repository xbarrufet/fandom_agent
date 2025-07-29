

def get_text_from_brackets(text: str) -> str:
    """
    Extracts the first textL found in the given text between square brackets [].

    Args:
        text (str): The input text containing a URL.
    Returns:
        str: the text within []
    """
    start = text.find('[')
    end = text.find(']', start)
    if start != -1 and end != -1:
        return text[start + 1:end]
    return ""