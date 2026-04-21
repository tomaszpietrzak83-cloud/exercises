def from_roman_numeral(roman_numeral):
    roman_numeral = roman_numeral[::-1]
    value = 0
    previousCharacterValue = 0
    counter = 1
    previousCharacter = None

    for i, character in enumerate(roman_numeral):
        characterValue = romanValues[character]

        if characterValue < previousCharacterValue:
            value -= characterValue
            previousCharacterValue = characterValue
        else:
            value += characterValue
            previousCharacterValue = characterValue

        if character == previousCharacter:
            counter += 1
        else:
            counter = 1

        if character in ("V", "L", "D"):
            if counter > 1:
                print("V, L, D can appear once.")
                raise ValueError
        else:
            if counter > 3:
                print("Theres more than 3 same characters in roman number.")
                raise ValueError

        previousCharacter = character

    return value


romanValues = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
try:
    print(from_roman_numeral("MMCDLXXVIII"))
except ValueError:
    print("Please enter proper number.")
