name = "Yossi"
age = 40

# if name == "Yossi":
#     print(f"Hello {name}")
# else:
#     print("I dont recognise you - Terminating")

if name == "Yossi":
    print(f"Hello {name}")
elif age > 30:
    print (f"Your age is higher than 30")
else:
    print("I dont recognise you - Terminating")


# and
# or

sky_color = "Blue"
print(10<20 and sky_color == "Blue") # True

sky_color = "Red"
print(10 < 20) or (sky_color == "Blue") #  or - at least 1 condition to result in True
print(10 > 20) and (sky_color == "Blue") #  and - needs at least 1 condition to return False to result in False

