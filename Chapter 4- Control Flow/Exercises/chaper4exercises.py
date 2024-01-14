#Exercise 1:  Alien Colors #1
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")

alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!")

#Exercise 2: Alien Colors #2
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")

if alien_color != "green":
    print("You just earned 10 points!")

alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#Exercise 3: Alien Colors #3
alien_color = "green"
if alien_color == "yellow":
    print("You just earned 10 points!")
elif alien_color == "red":
    print("You just earned 15 points!")
else:
    print("You just earned 5 points!")

alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "red":
    print("You just earned 15 points!")
else:
    print("You just earned 10 points!")

alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

#Exercise 4: Stages of Life
age = 15
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

#Exercise 5: Favorite Fruit
favorite_fruits = ["grapes", "watermelon", "orange"]

if "watermelon" in favorite_fruits:
    print("You really like watermelon!")
if "apple" in favorite_fruits:
    print("You really like apples!")
if "orange" in favorite_fruits:
    print("You really like oranges!")
if "pineapple" in favorite_fruits:
    print("You really like pineapples!")
if "grapes" in favorite_fruits:
    print("You really like grapes!")
