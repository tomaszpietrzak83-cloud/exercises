text = "A tiny fox wandered through an extraordinarily quiet forest, '\
where shimmering leaves whispered secrets to anyone patient enough to listen. '\
Suddenly, it encountered a peculiar machine, humming softly beneath a crooked oak tree, '\
blinking with multicolored lights and producing an oddly comforting rhythm. '\
Curious yet cautious, the fox circled the device, '\
sniffing the metallic surface and tapping it gently with a paw. '\
Unexpectedly, the machine projected a vast, luminous map into the air, '\
revealing hidden paths, forgotten rivers, '\
and impossible mountains that seemed to breathe. '\
Mesmerized, the fox decided that adventure, '\
however unpredictable, was undeniably worth pursuing."


def countLetters(phrase):

    strangeCharacters = [
        "!",
        "?",
        ".",
        ",",
        ";",
        ":",
        "-",
        "_",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        '"',
        "'",
    ]

    for char in strangeCharacters:
        phrase = phrase.replace(char, "")

    words = phrase.split()

    numberOfLettersInEachWord = []
    for word in words:
        wordLength = len(word)
        numberOfLettersInEachWord.append(wordLength)

    print(numberOfLettersInEachWord)

    userInput = input(
        "Do you want to know how many of each number there is ([Y]es/[N]o)"
    )

    maxWordLength = max(numberOfLettersInEachWord)

    if userInput.lower() == "y":
        for number in range(maxWordLength):
            if number in numberOfLettersInEachWord:
                numberOfNumbers = numberOfLettersInEachWord.count(number)
                print(
                    f"There {'is' if numberOfNumbers == 1 else 'are'} {numberOfNumbers} "
                    f"{number}-letter word{'' if numberOfNumbers == 1 else 's'} in the phrase"
                )
    else:
        exit()


print(countLetters(text))
