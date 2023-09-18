#!/usr/bin/python3
"""prints adouble new line at points: """


def text_indentation(text):
    """prints adouble new line at points: """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    
    sen = ""
    a = 0
    while a < len(text):
        if text[a] is not "." and text[a] is not "?" and text[a] is not ":":
            sen += text[a]
        else:
            sen += text[a]
            print(sen)
            print()
            sen = ""
            while a < (len(text) - 1) and text[a+1] == " ":
                a += 1
        a += 1
    print(sen, end="")