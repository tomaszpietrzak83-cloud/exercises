# Sort letters of string in alphabetical order
phrase = "Something is Wrong with this string"


def sortCharacters(text):

    characters = list(text)

    characters.sort()

    sorted_string = "".join(characters)
    if " " in sorted_string:
        response = input("Do you want to remove spaces? (yes/no): ")

        if response.lower() == "yes" or "y":
            sorted_string = sorted_string.replace(" ", "")

    if not sorted_string.islower():
        response = input("Do you want to convert all letters to lowercase? (yes/no): ")

        if response.lower() == "yes" or "y":
            sorted_string = sorted_string.lower()
            letters = list(sorted_string)
            letters.sort()
            sorted_string = "".join(letters)

        else:
            return sorted_string

    return sorted_string


print(sortCharacters(phrase))
