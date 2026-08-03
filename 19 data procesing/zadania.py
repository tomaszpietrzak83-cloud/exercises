from dane import obecnosc, uczniowie


#  Przejrzyj dane i wyszukaj w nich informacje:
# - o klasie z najlepszą obecnością,
# - najlepszym uczniu z każdej klasy,
# - najlepszym uczniu ogółem,
# - czy któraś z klas miała średnią min 4.75?
# - czy któraś z klas miała obecność minimum 90%?
# - wskaż uczniów ze średnią minimum 4.0 którzy jednocześnie mają żadnej oceny poniżej -3.
# - policz wynik klasy i posortuj klasę malejąco względem wzoru `wynik = średnia_ocen * 0.7 + obecność * 0.3`
# - wskaż najtrudniejszy i najłatwiejszy przedmiot (najniższa i najwyższa srednia ocen)
# - wskaż leniwych ale zdolnych (obecość <70%, ocena >=4.5) i pracowitych ale nie tak zdolnych (obecność >=90%, ocena <3.5)
# - uczniów z tylko kiepskimi ocenami (żadna z ocen nie przekracza 3.3)
# - wymień uczniów, którzy byli obecni co najmneij 10 dni pod rząd

uczniowieLines = uczniowie.split("\n")

studentsLines = []
gradesDict = {}
keyList = []
for idx, line in enumerate(uczniowieLines):
    if line == "":
        continue

    if idx == 0:
        keyList = line.split(";")
    else:
        studentsLines.append(line.split(";"))


for idx, line in enumerate(studentsLines):
    personName = line[0]
    personDict = dict(zip(keyList[1:], line[1:]))
    gradesDict.update({personName: personDict})

presence = {
    "1A": [],
    "1B": [],
    "1C": [],
}

for key, line in obecnosc:
    if line == "":
        continue
    StudentClass = gradesDict[key["klasa"]]
    average = 0
    counter = 0
    present = 0
    for character in line:
        if character == "O":
            counter += 1
        else:
            counter += 1
            present += 1
    average = present / counter

    match StudentClass:
        case "1A":
            presence["1A"].append(average)
        case "1B":
            presence["1B"].append(average)
        case "1C":
            presence["1C"].append(average)
averagePresence = {
    "1A": sum(presence["1A"]) / len(presence["1A"]),
    "1B": sum(presence["1B"]) / len(presence["1B"]),
    "1C": sum(presence["1C"]) / len(presence["1C"]),
}
