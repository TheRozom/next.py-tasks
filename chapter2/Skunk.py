from Animal import Animal


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self.stink_count_ = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")
