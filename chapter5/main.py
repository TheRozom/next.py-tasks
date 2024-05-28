class IDIterator:
    """
    Iterator class to generate valid ID numbers.

    Attributes:
        id (int): The current ID number.
    """

    def __init__(self, id):
        """
        Initialize the iterator with the starting ID.

        Args:
            id (int): The starting ID number.
        """
        self.id = id

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            IDIterator: The iterator object itself.
        """
        return self

    def __next__(self):
        """
        Generate the next valid ID number.

        Returns:
            int: The next valid ID number.

        Raises:
            StopIteration: If the ID exceeds the maximum limit.
        """
        self.id += 1
        while not check_id_valid(self.id):
            if self.id > 999_999_999:
                raise StopIteration
            self.id += 1

        return self.id


def id_generator(start_id):
    """
    Generator function to yield valid ID numbers.

    Args:
        start_id (int): The starting ID number.

    Yields:
        int: The next valid ID number.
    """
    current_id = start_id
    while current_id <= 999_999_999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1


def sum_digits(num):
    """
    Calculate the sum of digits in a number.

    Args:
        num (int): The number to sum digits of.

    Returns:
        int: The sum of the digits.
    """
    return sum(int(digit) for digit in str(num))


def check_id_valid(id_number):
    """
    Check if the ID number is valid.

    Args:
        id_number (int): The ID number to check.

    Returns:
        bool: True if the ID is valid, False otherwise.
    """
    id_digits = list(str(id_number))
    id_digits = [int(digit) * ((i % 2) + 1) for i, digit in enumerate(id_digits)]
    id_sum = sum(sum_digits(num) for num in id_digits)
    return id_sum % 10 == 0


def main():
    """
    Main function to prompt user input and generate IDs.

    Prompts the user to enter an ID and choose between generating IDs
    using an iterator or a generator, then prints the next 10 valid IDs.
    """
    input_id = int(input("Enter ID: "))
    choice = input("Generator or Iterator? (gen/it)? ")

    if choice == "it":
        id_iterator = IDIterator(input_id)
        for _ in range(10):
            print(next(id_iterator))
    else:
        id_gen = id_generator(input_id)
        for _ in range(10):
            print(next(id_gen))


if __name__ == "__main__":
    main()
