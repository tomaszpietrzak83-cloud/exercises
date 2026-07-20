# Write a function named missing_card that given a card game returns the (single) missing card name.

# The card game will be given as a single string of space-separated cards names.

# A card is represented by its color and value, the color being in {"S", "H", "D", "C"} and the value being in {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}, for a total of 52 possibilities.

# You'll always be given 51 cards, and you have to return the missing one.
from random import randint


def randomCardGenerator():
    color = cardsColors[randint(0, 3)]
    value = cardsValues[randint(0, 12)]
    randomCard = color + value
    randomCard = {randomCard}
    return randomCard


def missing_card(cardsSet):
    missingCard = allCards - cardsSet
    return missingCard


cardsColors = ("S", "H", "D", "C")
cardsValues = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

allCards = ""
for color in cardsColors:
    for value in cardsValues:
        card = color + value
        allCards += f" {str(card)}"

    allCards += "\n"
allCards = set(allCards.split())

riddle = allCards - randomCardGenerator()
print(sorted(list(riddle)))
print(missing_card(riddle))
