def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    length = len(text)

    while i < length:
        result += text[i]
        if text[i] in ".?:":
            result = result.rstrip()  # Remove trailing spaces before adding new lines
            result += "\n\n"
            i += 1  # Move to the next character
            # Skip all spaces after the punctuation mark
            while i < length and text[i] == ' ':
                i += 1
            continue  # Continue without incrementing i again
        i += 1

    print(result.rstrip(), end="")  # Prevent print() from adding a newline
