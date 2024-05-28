def get_longest_name():
    """
    Retrieves the longest name from the file.

    Returns:
        str: The longest name found in the file.
    """
    with open("names.txt", "r") as file:
        return max(file.read().split("\n"))


def get_total_name_length():
    """
    Calculates the total length of all names in the file.

    Returns:
        int: The total length of all names.
    """
    with open("names.txt", "r") as file:
        return sum(len(name) for name in file.read().split("\n"))


def get_shortest_names():
    """
    Retrieves the shortest name(s) from the file.

    Prints:
        str: The shortest name(s) found in the file.
    """
    with open("names.txt", "r") as file:
        names = [name.strip() for name in file if name.strip("\n")]
        min_len = min(len(name) for name in names)
        [print(name) for name in names if len(name) == min_len]


def save_name_lengths():
    """
    Saves the lengths of all names to a new file.

    Creates a new file "names_length.txt" and writes the length of each name to it.
    """
    with open("names.txt", "r") as file:
        with open("names_length.txt", "w") as file2:
            file2.writelines([str(len(name.strip())) + "\n" for name in file.readlines()])


def filter_names_by_length():
    """
    Filters names in the file based on user input length.

    Prompts the user to input a name length and prints names of that length.
    """
    number = int(input("Enter name length: "))
    with open("names.txt", "r") as file:
        print("\n".join(name for name in file.read().split("\n") if len(name) == number))


def main():
    print("1. Longest name:", get_longest_name())
    print("2. Total name length:", get_total_name_length())
    print("3. Shortest names:")
    get_shortest_names()
    save_name_lengths()
    filter_names_by_length()


if __name__ == "__main__":
    main()
