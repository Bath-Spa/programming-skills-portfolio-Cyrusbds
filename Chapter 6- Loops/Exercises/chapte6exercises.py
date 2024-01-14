#Exercise 1: Pizza Toppings
pizza = input("Enter a series of pizza toppings on your pizza: ")
print(pizza, "has been added to the pizza.")
while pizza != "quit":
    pizza = input("Enter a series of pizza toppings on your pizza: ")
    print(pizza, "toppings has been added to your pizza.")

#Exercise 2: Movie Tickets
age = int(input("What is your age? "))
if age < 3:
    print("Your ticket is Free")
elif age < 12:
    print("Your ticket is $10")
else:
    print("Your ticket is $15")
while age != 0:
    age = int(input("What is your age? "))
    if age < 3:
        print("Your ticket is Free")
    elif age < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")

#Exercise 3: Infinity  
loop = "This loop never ends"
while loop != 0:
    print(loop)

#Exercise 4: Deli
sandwich_orders = ["ham", "chicken", "egg", "bacon"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

#Exercise 5: No Pastrami
sandwich_orders = ["ham", "pastrami", "chicken", "pastrami", "egg", "pastrami", "bacon"]
finished_sandwiches = []
print("the deli has run out of pastrami\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")