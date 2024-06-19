# --1--Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {1,8,22,23,24,74}
print(my_fav_numbers)
my_fav_numbers.add(15)
my_fav_numbers.add(20)
print(my_fav_numbers)
my_fav_numbers.pop() #or .remove or .pop
print(my_fav_numbers)
friend_fav_numbers  = {2,3,4}
our_fav_numbers = (my_fav_numbers.union(friend_fav_numbers ))
print(our_fav_numbers)

# --2-- Tuples are unchangeable


# --3--Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
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

#--4-- Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?
float_set = {1.5,2.5,3.5,4.5}
int_set = {2,3,4,5}
print(float_set.union(int_set))
# ... can not solve this task

# --5--Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for i in range(1, 21):
    print(i)
for i in range(1,21):
    if i%2==0:
        print(i)

# --6- Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
guess_who = True
while guess_who:
     name = input('Guess Who? ')
     if name == "Me":
        guess_who = False

#--7-- Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
fav = input("Enter your fav fruits in a string with a space between: ")
basket = fav.split()
print(basket)
fruit = input("Enter a name of any fruit on this Earth: ")
    if fruit in basket: # i can not solve
        print("You chose one of your favorite fruits! Enjoy!")
    else:
        print("You chose a new fruit. I hope you enjoy")

# --8--Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
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
    

# --9--A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.



# --10 -- Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich