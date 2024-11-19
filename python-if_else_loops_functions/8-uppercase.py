#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Convertir en majuscule si c'est une lettre minuscule
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
