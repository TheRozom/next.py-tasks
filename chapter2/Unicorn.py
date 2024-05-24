from Animal import Animal


class Unicorn(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")
