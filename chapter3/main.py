class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, illegal_char):
        self.username = username
        self.illegal_char = illegal_char

    def __str__(self):
        return f"The username '{self.username}' contains an illegal character: '{self.illegal_char}'"


class UsernameTooShort(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"The username '{self.username}' is too short."


class UsernameTooLong(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"The username '{self.username}' is too long."


class PasswordMissingCharacter(Exception):
    pass


class PasswordTooShort(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"The password '{self.password}' is too short."


class PasswordTooLong(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"The password '{self.password}' is too long."


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return f"The password is missing a character (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return f"The password is missing a character (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return f"The password is missing a character (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return f"The password is missing a character (Special)"


def check_input(username, password):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    punctuation = "!@#$%^&*()_+-=.,/"

    has_upper = False
    has_lower = False
    has_digit = False
    has_punct = False

    if any(char not in upper + numbers + lower for char in username):
        raise UsernameContainsIllegalCharacter(
            username,
            next(
                (char for char in username if char not in upper + numbers + lower), None
            ),
        )
    if len(username) < 3:
        raise UsernameTooShort(username)
    if len(username) > 16:
        raise UsernameTooLong(username)
    if len(password) < 8:
        raise PasswordTooShort(password)
    if len(password) > 40:
        raise PasswordTooLong(password)

    for char in password:
        if char in upper:
            has_upper = True
        elif char in lower:
            has_lower = True
        elif char in numbers:
            has_digit = True
        elif char in punctuation:
            has_punct = True

    if not has_upper:
        raise PasswordMissingUppercase()
    if not has_lower:
        raise PasswordMissingLowercase()
    if not has_digit:
        raise PasswordMissingDigit()
    if not has_punct:
        raise PasswordMissingSpecial()

    print("OK")


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            check_input(username, password)
            print("Login successful!")
            break  # Exit the loop if input is valid
        except (
            UsernameContainsIllegalCharacter,
            UsernameTooShort,
            UsernameTooLong,
            PasswordMissingCharacter,
            PasswordTooShort,
            PasswordTooLong,
            PasswordMissingUppercase,
            PasswordMissingLowercase,
            PasswordMissingDigit,
            PasswordMissingSpecial,
        ) as e:
            print(f"Invalid input: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
