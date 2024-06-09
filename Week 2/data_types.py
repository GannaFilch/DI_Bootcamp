print("hello world!")

# [0 0 0 0 0 0 0 0] - 1 byte - 8bits

# Strings - data type for representing text
# "" - str "hello"
# '' - str 'hello'

print("Hello world!") # <- prints Hello World! on the screen
print("Hello " + "World")

# operations (mathematical) - +, -, *, /

# methods - like functions that are used from (not on) a certain data type/object

print("A string".capitalize())
print("Blah".index("l"))
print("BBBB".lower())

name= "Ron"
print(f"Hello {name}")

# int - integer

print(10 + 100) # addition
print(2 * 2) # multiplication
print(2 ** 3) # to the power
print(100 / 10) # division
print(99 / 10)
print(99 // 10) # divides and floors/roundsthe number to the lower bound

print(3*(1+2) + 99 // 10)

# float - floating numbers

a_float = 10.1020
b_float = 11.0

print(2*2.0) # floats takes over

# variable - a placeholder for a value/data ctructure

a_string = "Hello"

number_a = 10
number_b = 12

print(number_a + number_b)

a_boolean = Trueb_boolean = False
deposit = 200
birthdate = 1999

print(f"Yossi was born on {birthdate}, and he has {deposit} on his bank account")

number1 = 10
number2 = 100

print(number1 == number2) # False - bool

# == - equals ?

print("AA" == 'aa') # False

print(number1 < number2) # True
print(number1 > number2) # False


number3 = 10

print(number1 < number3) # False
print(number1 <= number3) # Less or Equal - True

# != - not equals ?

print(number1 != number2) # Trie = not equal
print(number1 != number3) # False - equal