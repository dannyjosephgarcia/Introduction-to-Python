class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

    def sleeping(self):
        print("I'm sleeping")

    def eating(self):
        print("I'm eating")


class Dog(Animal):
    def __init__(self, num_legs, demeanor):
        super().__init__(num_legs)
        self.demeanor = demeanor

    def speak(self):
        print("Woof")


class Cat(Animal):
    def __init__(self, num_legs, demeanor):
        super().__init__(num_legs)
        self.demeanor = demeanor

    def speak(self):
        print("Meow")


if __name__ == "__main__":
    animal = Animal(4)
    print(animal.sleeping())
    print(animal.eating())
    dog = Dog(4, "Friendly")
    cat = Cat(4, "Angry")
    print(dog.demeanor)
    print(dog.num_legs)

