#!/usr/bin/python3
"""
This module provides a function for text formatting with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after `.`, `?`, and `:`.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result = result.rstrip()  # Remove trailing spaces before adding new lines
            result += "\n\n"
        i += 1

    print(result.strip())  # Ensure no leading or trailing spaces
