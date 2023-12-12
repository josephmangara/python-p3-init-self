#!/usr/bin/env python3

class Dog:
    def __init__(self, name, age, breed="Mutt"):
        self.name = f"name: {name}"
        self.breed = f"breed: {breed}"
        self.age = f"age: {age}"

    def adopt(self, owner_name):
        self.owner = owner_name

snoopy = Dog("Snoppy", "3", "Rottweiler")
print(snoopy.breed)
print(snoopy.age)

# fido = Dog("Fido")
# fido.adopt("Sophie")
# print(fido.owner)
# print(fido is fido.showing_self())
