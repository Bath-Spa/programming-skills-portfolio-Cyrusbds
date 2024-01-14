def fun():
    print("This is a Function")

fun()


def my_function(fname):
    print(" Hi, " + fname)

my_function("Cyrus")
my_function("Cyrus")
my_function("Cyrus")


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Cyrus", "DS")
my_function("Cyrus", "DS")
my_function("Cyrus", "DS")


def my_function(fname="Cyrus", lname="DS"):
    print("My full name is " + fname + " " + lname)

my_function()