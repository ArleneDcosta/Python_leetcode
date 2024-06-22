from typing import Type


class Animal:
    @classmethod
    def make_sound(cls):
        print("A sound is made")


def mimic(animal_class: Type[Animal]):  # animal_class is a class, not an instance
    animal_class.make_sound()


print(mimic(Animal))
