# 1
with open("names.txt", "r") as file:
    print(max(file.read().split("\n")))

# 2
with open("names.txt", "r") as file:
    print(sum(len(name) for name in (file.read().split("\n"))))

# 3
with open("names.txt", "r") as file:
    names = [name.strip() for name in file if name.strip("\n")]
    min_len = min(len(name) for name in names)
    [print(name) for name in names if len(name) == min_len]

# 4
with open("names.txt", "r") as file:
    with open("names_length.txt", "w") as file2:
        file2.writelines([str(len(name.strip())) + "\n" for name in file.readlines()])

# 5
number = int(input("Enter name length: "))
with open("names.txt", "r") as file:
    print("\n".join(name for name in file.read().split("\n") if len(name) == number))
