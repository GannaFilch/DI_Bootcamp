# 🌟 Exercise 3 : Dogs Domesticated
class Dog:
    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return self.weight / self.age * 10
     


# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
class PetDog(Dog):
    def __init__(self, name, age, weight, trained:bool = False):
        super().__init__(name, age, weight)
        self.trained = trained
    def trained(self):
        return super().bark()
    def play(self, name):
        for Dog in Dogs:
            print(f'{Dogs[self.name]} playin together')
    def do_a_trick(self, name):
        # if self.trained = True
        good_boy = [f'{Dog[self.name]} does a barrel roll', f'{Dog[self.name]} stands on his back legs', f'{Dog[self.name]} shakes your hand', f'{Dog[self.name]} playes dead' ]
        if self.trained = True
        return(print)
        
Dog1 = Dog('Jojo', 4, 5.9)
Dog2 = Dog('Juju', 11, 9.5)
Dog3 = Dog('Jiji', 15, 16)  
Dogs = (Dog1, Dog2, Dog3)
Dog1.do_a_trick()



# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

