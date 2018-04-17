#Maria Loren I. Ignacio
#https://github.com/lorenignacio
#lorenignacio00@gmail.com


def only_upper(s):
    upper_chars = ("Thank God for everything")
    for char in s:
        if char.isupper():
            upper_chars += char
    return upper_chars

only_upper(s)
