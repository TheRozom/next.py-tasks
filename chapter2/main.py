from Animal import Animal
from Cat import Cat
from Dog import Dog
from Skunk import Skunk
from Unicorn import Unicorn
from Dragon import Dragon


def main():
    """
    Main function to create a list of zoo animals and perform actions based on their type.

    For each animal, if it is hungry, it will be fed until it is no longer hungry.
    Each animal will then perform its talk method, and if it has specific methods (fetch_stick, chase_laser, etc.),
    those will be called as well.
    """
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80),
    ]

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
