# --1--Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
def display_message():
    message = "Im learning functions today"
    print(message)

display_message()

# --2--Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f'{title} is my favorite book')

favorite_book('Python for dummies')

# --3--Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country):
    print(f'{city} is in {country}')

describe_city('jerusalem','israel')
describe_city('st petersburg','russia')

# --4--Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

# from random import randint // randint(1, 100))

from random import randint
def random(b):
    a = randint(1,100)
    if () == a:
        print("Nice")
    else:
        print(f'sorry. your lucky num is: {a} , but you chose: {b}')
b = input("from 1 to 100: ")
random(b)

# --5-- Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

#1-3
def make_shirt(size, text):
    print(f'I need a {size} size tshirt')
    print(f'with a printed "{text}" text on it')

make_shirt('large', 'i love python')

#4-7
def make_shirt(size='large', text='i love python'):
    print(f'I need a {size} size tshirt')
    print(f'with a printed "{text}" text on it')

print(make_shirt(size='medium'))
print(make_shirt(size='small', text='not sure about love'))

#8
def make_shirt(size='large', text='i love python'):
    print('make_shirt: ', size, text) #-- doesnt work, why?


