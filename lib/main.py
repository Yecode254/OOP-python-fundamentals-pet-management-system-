# class initialisation with default init 
class Pet:
    def speak(self):
        # print("Sound made !")
        return("Pet spoke")

Rasmus = Pet()
Rasmus.name = "Rasmus"
print(Rasmus.name)
print(Rasmus.speak())
 
#  A simple class to represent a dog with modified  __init__
class Dog:
    species = "Canis_lupaz_familiaris"
    def __init__(self,name,breed,age="N/A"):
        self.name = name
        self.breed = breed
        self.age = age 

    def speak(self):
        return (f"{self.name} say woof! woof!")
        
koba = Dog("Koba","Great Dane",3)
amad= Dog ("Amad", "GermanShephard")
koba.age = 4
print(koba.speak())
print(koba.age)
print(amad.age)
print(amad.species)==print(koba.species)
class Cat:
    pass
class Rat:
    pass