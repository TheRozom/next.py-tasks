class IDIterator:
    """Iterator class to generate valid ID numbers."""

    def __init__(self, id):
        self.id = id

    def __iter__(self):
        return self

    def __next__(self):
        self.id = self.id + 1
        while not check_id_valid(self.id):
            if self.id > 999999999:
                raise StopIteration
            self.id = self.id + 1

        return self.id


def id_generator(start_id):
    """Generator function to yield valid ID numbers."""
    current_id = start_id
    while current_id <= 999999999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1


def sum_digits(num):
    """Calculate the sum of digits in a number."""
    return sum(int(digit) for digit in str(num))


def check_id_valid(id_number):
    """Check if the ID number is valid."""
    id = list(str(id_number))
    id = [int(digit) * ((i % 2) + 1) for i, digit in enumerate(id)]
    id_sum = sum(sum_digits(num) for num in id)
    return id_sum % 10 == 0


def main():
    """Main function to prompt user input and generate IDs."""
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
