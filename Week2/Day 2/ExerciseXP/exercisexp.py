

my_fav_numbers = {1,8,22,23,24,74}
print(my_fav_numbers)
my_fav_numbers.add(15)
my_fav_numbers.add(20)
print(my_fav_numbers)
my_fav_numbers.discard(74)
print(my_fav_numbers)
friend_fav_numbers  = {2,3,4}
our_fav_numbers = (my_fav_numbers.union(friend_fav_numbers ))
print(our_fav_numbers)

# Tuples are unchangeable

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket[1:])
print(basket[:-1])
basket.append("Kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples"))
basket.clear( )
print(basket)

float_set = {1.5,2.5,3.5,4.5}
int_set = {2,3,4,5}
print(float_set.union(int_set))
# ... can not solve this task

for i in range(1, 21):
    print(i)
for i in range(1,21):
    if i%2==0:
        print(i)

guess_who = True
while guess_who:
     name = input('Guess Who? ')
     if name == "Me":
        guess_who = False

fav = input("Enter your fav fruits in a string with a space between: ")
basket = fav.split()
print(basket)
fruit = input("Enter a name of any fruit on this Earth: ")
    if fruit in basket: # i can not solve
        print("You chose one of your favorite fruits! Enjoy!")
    else:
        print("You chose a new fruit. I hope you enjoy")

print("Input Quit when is enough for you")
str = "Which topping you would like to add? "
while True:
    topping = input(str)
    if topping == "Quit":
       break 
    else:
        print("We will add " + topping + " to the pizza")
print("Your toppings choise: ")
print(type(topping)) # do not know how to finish this tsk and solve the next ones.. sorry
    