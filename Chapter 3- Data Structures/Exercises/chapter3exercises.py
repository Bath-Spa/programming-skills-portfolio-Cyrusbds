#Exercise 1: Names
names = ["Mark", "John", "Joseph", "Andrei"]
for name in names:
    print(name)

#Exercise 2: Greetings
names = ["Mark", "John", "Joseph", "Andrei"]
for name in names:
    print("Hello", name, ", How are you?")

#Exercise 3: Your Own List
transportation = ["Tesla Car", "Double Deck Bus", "Fastest Train", "High Class Airplane"]
for transpo in transportation:
    print("I would like to ride a", transpo, ".")

#Exercise 4: Guest List
invitees = ["Mark", "John", "Joseph"]
for invite in invitees:
    print("Hello", invite,", Would you like to go out and eat dinner?")

#Exercise 5: Change Guest List
invitees = ["Mark", "John", "Joseph"]
print(invitees)
print(invitees[1], "Can't make it to dinner.")
invitees.remove("John")
invitees.insert(1,"Andrei")
print(invitees)
for invitee in invitees:
    print("Hello", invitee,", Would you like to go out and eat dinner?")

#Exercise 6: Shrinking Guest List
invitees = ["Mark", "Andrei", "Joseph"]
print("Sorry, but I can invite only two people for dinner.")
popped_invitees = invitees.pop()
print("I'm Sorry",  popped_invitees ,"I can't invite you to dinner.")
for invitee in invitees:
    print("Hello", invitee, "You are still invited to dinner.")
del invitees[:]
print(invitees)

#Exercise 7: Seeing the World
places = ["Tokyo", "France", "Moon", "America", "Germany"]
print("Original order:")
print(places)
print("Alphabetical order:")
print(sorted(places))
print("Original order:")
print(places)
print("Reverse alphabetical order:")
print(sorted(places, reverse=True))
print("Original order:")
print(places)
places.reverse()
print("Reversed order:")
print(places)
places.reverse()
print("Original order:")
print(places)
places.sort()
print("Alphabetical order:")
print(places)
places.sort(reverse=True)
print("Reverse alphabetical order:")
print(places)
