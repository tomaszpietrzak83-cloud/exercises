phrase = "A tiny fox wandered through an extraordinarily quiet forest, '\
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

strangeCharacters = ['!', '?', '.', ',', ';', ':', '-', '_', '(', ')', '[', ']', '{', '}', '"', "'"]

stripPhrase = phrase

for char in strangeCharacters:
    stripPhrase = stripPhrase.replace(char, '')

stripPhrase = stripPhrase.split()

numberOfLettersInEachWord = []

for word in stripPhrase:
    wordLength = len(word)    
    numberOfLettersInEachWord.append(wordLength)

print(numberOfLettersInEachWord)

userInput = input("Do you want to know how many of each number there is ([Y]es/[N]o)")

def numberCounter (listOfNumbers, specificNumber):
    counter = 0
    for element in listOfNumbers:
        if element == specificNumber:
            counter += 1
    return counter

if userInput.lower() == "y":

    for number in range(30): #i dont know what is longest word

        if number in numberOfLettersInEachWord:

            numberOfNumbers = numberOfLettersInEachWord.count(number)
            print(f"There are {numberOfNumbers} {number}-letter word{"" if {number} == 1  else "s"} in phrase")


else:
    exit()
