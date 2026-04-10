roleTable = {
    "Warrior": {"HP": 100, "MP": 50, "Strength": 20, "Agility": 10, "Intelligence": 5},
    "Mage": {"HP": 70, "MP": 100, "Strength": 5, "Agility": 10, "Intelligence": 20},
    "Rogue": {"HP": 80, "MP": 60, "Strength": 15, "Agility": 15, "Intelligence": 5},
    "Tank": {"HP": 170, "MP": 30, "Strength": 25, "Agility": 5, "Intelligence": 5},
    "Paladin": {"HP": 120, "MP": 80, "Strength": 15, "Agility": 10, "Intelligence": 10}
}

raseTable = {
    "Human": {"HP": 20, "MP": 20, "Strength": 5, "Agility": 5, "Intelligence": 5},
    "Elf": {"HP": 10, "MP": 30, "Strength": 5, "Agility": 10, "Intelligence": 10},
    "Dwarf": {"HP": 30, "MP": 10, "Strength": 10, "Agility": 5, "Intelligence": 5},
    "Orc": {"HP": 40, "MP": 5, "Strength": 15, "Agility": 5, "Intelligence": 0},
    "Troll": {"HP": 50, "MP": 0, "Strength": 20, "Agility": 0, "Intelligence": -5}
}

classNameTable = {
    "High": {"HP": 20, "MP": 20, "Strength": 5, "Agility": 5, "Intelligence": 5},
    "Tough": {"HP": 30, "MP": 10, "Strength": 10, "Agility": 5, "Intelligence": 5},
    "Agile": {"HP": 10, "MP": 30, "Strength": 5, "Agility": 10, "Intelligence": 10},
    "Intelligent": {"HP": 10, "MP": 30, "Strength": 5, "Agility": 5, "Intelligence": 15},
    "Balanced": {"HP": 20, "MP": 20, "Strength": 10, "Agility": 10, "Intelligence": 10}
}

person = {
    "person1": {
        "name": "John Doe",
        "class": "Balanced",
        "rase": "Human",
        "role": "Tank",
        "HP": roleTable["Tank"]["HP"] + raseTable["Human"]["HP"] + classNameTable["Balanced"]["HP"],
        "MP": roleTable["Tank"]["MP"] + raseTable["Human"]["MP"] + classNameTable["Balanced"]["MP"],
        "Strength": roleTable["Tank"]["Strength"] + raseTable["Human"]["Strength"] + classNameTable["Balanced"]["Strength"],
        "Agility": roleTable["Tank"]["Agility"] + raseTable["Human"]["Agility"] + classNameTable["Balanced"]["Agility"],
        "Intelligence": roleTable["Tank"]["Intelligence"] + raseTable["Human"]["Intelligence"] + classNameTable["Balanced"]["Intelligence"]
    },

    "person2": {
        "name": "Jane Smith",
        "class": "Agile",
        "rase": "Elf",
        "role": "Rogue",
        "HP": roleTable["Rogue"]["HP"] + raseTable["Elf"]["HP"] + classNameTable["Agile"]["HP"],
        "MP": roleTable["Rogue"]["MP"] + raseTable["Elf"]["MP"] + classNameTable["Agile"]["MP"],
        "Strength": roleTable["Rogue"]["Strength"] + raseTable["Elf"]["Strength"] + classNameTable["Agile"]["Strength"],
        "Agility": roleTable["Rogue"]["Agility"] + raseTable["Elf"]["Agility"] + classNameTable["Agile"]["Agility"],
        "Intelligence": roleTable["Rogue"]["Intelligence"] + raseTable["Elf"]["Intelligence"] + classNameTable["Agile"]["Intelligence"]
    }
}

def createPerson(name, className, rase, role):
    howManyInPerson = len(person) + 1
    personKey = f"person{howManyInPerson}"
    person[personKey] = {}
    person[personKey]["name"] = name
    person[personKey]["class"] = className
    person[personKey]["rase"] = rase
    person[personKey]["role"] = role
    person[personKey]["HP"] = roleTable[role]["HP"] + raseTable[rase]["HP"] + classNameTable[className]["HP"]
    person[personKey]["MP"] = roleTable[role]["MP"] + raseTable[rase]["MP"] + classNameTable[className]["MP"]
    person[personKey]["Strength"] = roleTable[role]["Strength"] + raseTable[rase]["Strength"] + classNameTable[className]["Strength"]
    person[personKey]["Agility"] = roleTable[role]["Agility"] + raseTable[rase]["Agility"] + classNameTable[className]["Agility"]
    person[personKey]["Intelligence"] = roleTable[role]["Intelligence"] + raseTable[rase]["Intelligence"] + classNameTable[className]["Intelligence"]
    print("Character created:")
    print("Name:", person[personKey]["name"])
    print("Class:", person[personKey]["class"])
    print("Race:", person[personKey]["rase"])
    print("Role:", person[personKey]["role"])
    print("HP:", person[personKey]["HP"])
    print("MP:", person[personKey]["MP"])
    print("Strength:", person[personKey]["Strength"])
    print("Agility:", person[personKey]["Agility"])
    print("Intelligence:", person[personKey]["Intelligence"])
    return person

print("Welcome to the character creator!")
command = input("What do you want to do? (create/inspect/exit): ").lower()

#while command not in ["create", "inspect", "exit"]:
 #   print("Invalid command. Please choose from create, inspect, exit.")

if command == "C" or command == "c":
    command = "create"
elif command == "I" or command == "c":
    command = "inspect"
elif command == "E" or command == "e":
    command = "exit"


while command != "exit":
    if command == "create":
        statPoints = 20
        name = input("Enter your character's name: ").lower().capitalize()
        print("Choose a class: High, Tough, Agile, Intelligent, Balanced")
        className = input("Enter your character's class: ").lower().capitalize()

        if className == "h" or className == "H":
            className = "High"
        elif className == "t" or className == "T":
            className = "Tough"
        elif className == "a" or className == "A":
            className = "Agile"
        elif className == "i" or className == "I":
            className = "Intelligent"
        elif className == "b" or className == "B":
            className = "Balanced"
            
        if className not in classNameTable:
            print("Invalid class. Please choose from High, Tough, Agile, Intelligent, Balanced.")
        
        print("Choose a race: Human, Elf, Dwarf, Orc, Troll")
        rase = input("Enter your character's race: ").lower().capitalize()
        if rase == "h" or rase == "H":
            rase = "Human"
        elif rase == "e" or rase == "E":
            rase = "Elf"
        elif rase == "d" or rase == "D":
            rase = "Dwarf"
        elif rase == "o" or rase == "O":
            rase = "Orc"
        elif rase == "t" or rase == "T":
            rase = "Troll"

        print("Choose a role: Warrior, Mage, Rogue, Tank, Paladin")
        role = input("Enter your character's role: ").lower().capitalize()
        if role == "w" or role == "W":
            role = "Warrior"
        elif role == "m" or role == "M":
            role = "Mage"
        elif role == "r" or role == "R":
            role = "Rogue"
        elif role == "t" or role == "T":
            role = "Tank"
        elif role == "p" or role == "P":
            role = "Paladin"

        character = createPerson(name, className, rase, role)

        print("You have", statPoints, "stat points to distribute.")
        while statPoints > 0:
            stat = input("Which stat do you want to increase? (HP/MP/Strength/Agility/Intelligence): ")
            if stat in ["Strength" or "s" or "S" or "strength", "Agility" or "a" or "A" or "agility", "Intelligence" or "i" or "I" or "intelligence"]:
                points = int(input(f"How many points do you want to add to {stat}? "))
                if points <= statPoints:
                    character[f"person{len(person)}"][stat] += points
                    statPoints -= points
                    print(f"{points} points added to {stat}. You have {statPoints} points left.")
                else:
                    print("You don't have enough stat points. Please try again.")
            elif stat in ["HP" or "h" or "hp", "MP" or "m" or "mp"]:
                points = int(input(f"How many points do you want to add to {stat}? It will add 5 to your {stat} per point. "))
                if points <= statPoints:
                    character[f"person{len(person)}"][stat] += 5 * points
                    statPoints -= points
                    print(f"{points} points added to {stat}. You have {statPoints} points left.")
                else:
                    print("You don't have enough stat points. Please try again.")
            else:
                print("Invalid stat. Please choose from HP, MP, Strength, Agility, Intelligence.")

    elif command == "inspect":
        for key, value in person.items():
            print(f"{key}: {value}")
    elif command == "exit":
        print("Goodbye!")
    command = input("What do you want to do? (create/inspect/exit): ").lower()
    print("Goodbye!")
