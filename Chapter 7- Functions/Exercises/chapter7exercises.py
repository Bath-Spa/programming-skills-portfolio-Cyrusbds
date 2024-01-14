#Exercise 1: Message
def display_message():
    print("I am learning how to make complicated codes easier")

display_message()

#Exercise 2: Favorite Book
def favorite_book(title):
    print("One of my favorite book is,", title)

favorite_book("The Diary of a Wimpy Kid")

#Exercise 3: T-Shirt
def make_shirt(size, text):
    print("The size of the shirt is", size, "and the message is", text)

make_shirt("Medium", "Just Do It")
make_shirt(size="Medium", text="Just Do It")

#Exercise 4:  Large Shirts
def make_shirt(size="Large", text="I Love Python"):
    print("The size of the shirt is", size, "and the message is", text)

make_shirt()
make_shirt("Medium", "Just Do It")
make_shirt("Small", "Never Give Up")
make_shirt("Extra Large", "Never Back Down")

#Exercise 5: Cities
def describe_city(city, country="Philippines"):
    print(city, "is in", country)

describe_city("Manila")
describe_city("Quezon")
describe_city("Tokyo", "Japan")