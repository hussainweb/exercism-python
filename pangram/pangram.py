def is_pangram(sentence):
    letters = set(sentence.lower())
    count = 0
    for letter in letters:
        if letter.isalpha():
            count += 1
    return count == 26
