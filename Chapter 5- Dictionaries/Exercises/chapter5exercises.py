#Exercise 1: Person
person = {"first_name": "Mark", "last_name": "Shang", "age": "22", "city": "Australia"}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

#Exercise 2: Glossary
glossary = {
    "Statements": "Execute in the order that they appear from top to bottom",
    "Function": "Piece of prewritten code that performs an operation",
    "String": "sequence of characters that is used as data",
    "Argument": "data given to a function",
    "Comments": "notes of explanation within a program"
}
for key, value in glossary.items():
    print(f"\n{key}: \n{value}")


#Exercise 3: Glossary 2
glossary = {
    "Statements": "Execute in the order that they appear from top to bottom",
    "Function": "Piece of prewritten code that performs an operation",
    "String": "sequence of characters that is used as data",
    "Argument": "data given to a function",
    "Comments": "notes of explanation within a program"
}
glossary["Variable"] = "The variable will act as a reference name for the user's input,"
glossary["Prompt"] = "string that informs the user of what data to enter"
glossary["List"] = "an ordered set of values, where each value is identified by an index"
glossary["Tuple"] = "disrupts the normal flow of instructions."
glossary["List"] = "An ordered and mutable collection of items in Python."
for key, value in glossary.items():
    print(f"\n{key}: \n{value}")

#Exercise 4: Rivers
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}
for key, value in rivers.items():
    print(f"The {key} runs through {value}.")
for key in rivers.keys():
    print(key)
for value in rivers.values():
    print(value)

#Exercise 5: Pets
pet1 = {'kind': 'Dog', 'owner': 'Mark'}
pet2 = {'kind': 'Cat', 'owner': 'John'}
pet3 = {'kind': 'Bird', 'owner': 'Andrei'}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"{pet['owner']}'s pet is a {pet['kind']}.")