from Animal import Animal
from Cat import Cat
from Dog import Dog
from Skunk import Skunk
from Unicorn import Unicorn
from Dragon import Dragon


def main():
    zoo_lst = []
    zoo_lst.append(Dog("Brownie", 10))
    zoo_lst.append(Cat("Zelda", 3))
    zoo_lst.append(Skunk("Stinky", 0))
    zoo_lst.append(Unicorn("Keith", 7))
    zoo_lst.append(Dragon("Lizzy", 1450))
    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))
    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__, animal.get_name())
            while animal.is_hungry():
                animal.feed()

        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(f"\nWelcome to {Animal.zoo_name}!")


if __name__ == "__main__":
    main()
