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
while command != "exit":
    if command == "create":
        name = input("Enter your character's name: ").lower().capitalize()
        print("Choose a class: High, Tough, Agile, Intelligent, Balanced")
        className = input("Enter your character's class: ").lower().capitalize()
        print("Choose a race: Human, Elf, Dwarf, Orc, Troll")
        rase = input("Enter your character's race: ").lower().capitalize()
        print("Choose a role: Warrior, Mage, Rogue, Tank, Paladin")
        role = input("Enter your character's role: ").lower().capitalize()
        character = createPerson(name, className, rase, role)
    elif command == "inspect":
        for key, value in person.items():
            print(f"{key}: {value}")
    elif command == "exit":
        print("Goodbye!")
    command = input("What do you want to do? (create/inspect/exit): ").lower()
    print("Goodbye!")
