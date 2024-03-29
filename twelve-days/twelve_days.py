allVerses = {
    1: "a Partridge in a Pear Tree",
    2: "two Turtle Doves",
    3: "three French Hens",
    4: "four Calling Birds",
    5: "five Gold Rings",
    6: "six Geese-a-Laying",
    7: "seven Swans-a-Swimming",
    8: "eight Maids-a-Milking",
    9: "nine Ladies Dancing",
    10: "ten Lords-a-Leaping",
    11: "eleven Pipers Piping",
    12: "twelve Drummers Drumming",
}

numbersToWord = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}


def getFirstLine(number):
    return f"On the {numbersToWord[number]} day of Christmas my true love gave to me: "


def getVerse(number):
    verses = reversed(allVerses)
    if number > 1:
        verses[number - 1] = "and " + verses[number - 1]
    verse = getFirstLine(number) + ", ".join(verses) + "."
    return verse


def recite(start_verse, end_verse):
    return [getVerse(verse) for verse in range(start_verse, end_verse + 1)]
