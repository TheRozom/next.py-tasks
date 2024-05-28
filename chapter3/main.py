class UsernameContainsIllegalCharacter(Exception):
    """
    Exception raised when the username contains an illegal character.

    Attributes:
        username (str): The username containing the illegal character.
        illegal_char (str): The illegal character found in the username.
    """

    def __init__(self, username, illegal_char):
        self.username = username
        self.illegal_char = illegal_char

    def __str__(self):
        return f"The username '{self.username}' contains an illegal character: '{self.illegal_char}'"


class UsernameTooShort(Exception):
    """
    Exception raised when the username is too short.

    Attributes:
        username (str): The username that is too short.
    """

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"The username '{self.username}' is too short."


class UsernameTooLong(Exception):
    """
    Exception raised when the username is too long.

    Attributes:
        username (str): The username that is too long.
    """

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"The username '{self.username}' is too long."


class PasswordMissingCharacter(Exception):
    """
    Base exception for missing character types in the password.
    """

    pass


class PasswordTooShort(Exception):
    """
    Exception raised when the password is too short.

    Attributes:
        password (str): The password that is too short.
    """

    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"The password '{self.password}' is too short."


class PasswordTooLong(Exception):
    """
    Exception raised when the password is too long.

    Attributes:
        password (str): The password that is too long.
    """

    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"The password '{self.password}' is too long."


class PasswordMissingUppercase(PasswordMissingCharacter):
    """
    Exception raised when the password is missing an uppercase character.
    """

    def __str__(self):
        return "The password is missing an uppercase character."


class PasswordMissingLowercase(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a lowercase character.
    """

    def __str__(self):
        return "The password is missing a lowercase character."


class PasswordMissingDigit(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a digit.
    """

    def __str__(self):
        return "The password is missing a digit."


class PasswordMissingSpecial(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a special character.
    """

    def __str__(self):
        return "The password is missing a special character."


def check_input(username, password):
    """
    Check the validity of the username and password based on several criteria.

    Args:
        username (str): The username to be validated.
        password (str): The password to be validated.

    Raises:
        UsernameContainsIllegalCharacter: If the username contains an illegal character.
        UsernameTooShort: If the username is too short.
        UsernameTooLong: If the username is too long.
        PasswordTooShort: If the password is too short.
        PasswordTooLong: If the password is too long.
        PasswordMissingUppercase: If the password is missing an uppercase character.
        PasswordMissingLowercase: If the password is missing a lowercase character.
        PasswordMissingDigit: If the password is missing a digit.
        PasswordMissingSpecial: If the password is missing a special character.
    """
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
    """
    Main function to handle user input and check username and password validity.

    Continuously prompts the user for a username and password until valid input is provided.
    Validates the input using the check_input function and prints appropriate messages for errors.
    """
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
