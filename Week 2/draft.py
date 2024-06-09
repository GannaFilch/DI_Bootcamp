# num = int(input("Enter a number from 1 to 100: "))
# # if num < 0 and num > 100:
# #     print("choose the number from 1 to 100")
# if num % 3 == 0:
#         print("Fizz")
# if num % 5 == 0:
#         print("Buzz")
# if num % 3 and num % 5:
#         print("FizzBuzz")

user_number = input("Please provide a number between 1 and 100: ")

user_number = int(user_number)

if 1 < user_number < 100:
    if (user_number % 15) == 0:
        print("FizzBuzz")
    elif (user_number % 3) == 0:
        print("Fizz")
    elif (user_number % 5) ==0:
        print("Buzz")
    
else: 
    print("Number is not in the correct range")

    
