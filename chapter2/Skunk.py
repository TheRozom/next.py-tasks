from Animal import Animal


class Skunk(Animal):
    """
    A class representing a skunk, inherited from Animal.

    Attributes:
        stink_count (int): The number of times the skunk can stink.

    Methods:
        talk(): Print the sound a skunk makes.
        stink(): Print the skunk stinking.
    """

    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initialize a Skunk instance.

        Args:
            name (str): The name of the skunk.
            hunger (int, optional): The hunger level of the skunk. Default is 0.
            stink_count (int, optional): The stink count of the skunk. Default is 6.
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        Make the skunk talk.
        """
        print("tsssss")

    def stink(self):
        """
        Make the skunk stink.
        """
        print("Dear lord!")
