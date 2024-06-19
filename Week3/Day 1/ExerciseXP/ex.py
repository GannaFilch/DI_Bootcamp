# 🌟 Exercise 1: Cats
# Instructions
# Using this class
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat('Gingy',12)
cat2 = Cat('Bubu', 7)
cat3 = Cat("Filimon", 18)
cats = [cat1, cat2, cat3]

def get_oldest_cat(cat_list: list[Cat]) -> Cat:

    oldest_cat = cat_list[0]

    for cat in cat_list:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    return oldest_cat

oldest_cat = get_oldest_cat(cats)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:

    def __init__(self, name: str, height: float) -> None:
        self.name = name
        self.height = height

    def bark(self) -> None:
        print(f"{self.name} goes woof!")

    def jump(self) -> None:
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

    def present(self):
        print(f"Dog name: {self.name}. Height: {self.height}")


def get_biggest_dog(dogs: list[Dog]) -> Dog:
    biggest_dog = max(dogs, key=lambda dog: dog.height)
    return biggest_dog


def main():

    ganna_dog = Dog(name="Dobby", height=20)
    ganna_dog.present()

    daniel_dog = Dog("Bonney", 23)
    daniel_dog.present()

    biggest_dog = get_biggest_dog([ganna_dog, daniel_dog])
    print(f"{biggest_dog.name} is the biggest dog!")


if __name__ == "__main__":
    main()



# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the sing_me_a_song method. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There's a lady who's sure",
                "all that glitters is gold", 
                "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()

# 🌟Exercise 4 : Afternoon At The Zoo ------DIDNT SOLVE---------------
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example
# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# Create a method called get_groups that prints the animal/animals inside each group.
# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo:
    def __init__(self, animals: list, zoo_name: str) -> None:
        self.animals = animals []
        self.zoo_name = zoo_name

    def add_animal(self, new_animal):
        #if new_animal not in self.animals ???
        self.animals.append(new_animal)

    def get_animal(self):
        print.animals
# animals = ()
# name = ZooLand