#!/usr/bin/python3

"""
prints a text with 2 new lines after each
instance of characters: ., ? and :
"""


def text_indentation(text):

    """
    text must be a string, else raise a TypeError exception
    (text must be a string)
    """

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    for i in range(len(text)):

        if text[i] == '.' or text[i] == '?' or text[i] == ':':

            print(text[i])
            print()

        else:

            print(text[i], end="")
