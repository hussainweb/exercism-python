def is_isogram(string):
    chars = {}
    for c in string.lower():
        if (c.isalpha() and c in chars.keys()):
            return False
        chars[c] = True
    return True
