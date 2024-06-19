
a = input("Enter a string with 10 characters only:")
if (len(a) > 10):
    print("string too long")
elif (len(a) < 10):   
    print("string too short")
else:
    print("perfect string")
res = a[0]
l = len(a)
res = res + a[l - 1]
print("First and Last:", res)

for i in range(len(a)):
    print(a[:i])

import random  # didnt find anoter way to solve this task :(
new_a = list(a)
random.shuffle(new_a)
print(new_a)  





