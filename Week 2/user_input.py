user_name = input("Please provide your username: ")

message = f"Hello {user_name}, nice to meet you!"

# print(message)

user_number = input("Provide a number between 1 and 100:")

# Type casting - turning one value type into another value type (str -> int)

user_number = int(user_number)
print(user_number)
print(type(user_number)) # atr, bool, int, float

print(user_number == 10)

# module operator - %
print(4 % 2)