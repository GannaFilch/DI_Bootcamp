
a= 'Hello World!'
print((a + ' ' + '\n')*5)


print((99 ** 3) * 8)

a = 3
b = 5
c = "3"
d = "Hello"
e = a
f = "hello"
print(b < a) #False
print(e == a) #True
print(a == c) #False
print(c > a) #TypeError: '>' not supported between instances of 'str' and 'int'
print(d == f) #False

computer_brand = "HP"
print("I have a " + computer_brand + " computer")

name = "Ganna"
age = 34
shoe_size = 38
info = (f'Shoes size of {name} is {shoe_size} and also she is {age} years old')
print(info)

        
a = 10
b = 8
if a > b:
    print("Hello World")        


num = int(input("Input a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

name = "Ganna"
input("What is your name:")
if name == "Ganna":
    print(f"Hi {name} Wow. Do people also joking that you are country?")


print("Are You Tall Enough To Ride A Roller Coaster?")
height = input("Please enter your height:")
height = int(height)
if (height >= 145):
    print("Enjoy your ride")
else:
    print("You need to grow up a little bit")




