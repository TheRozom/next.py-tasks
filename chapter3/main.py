import string

class UsernameException(Exception):
    """Base class for username-related exceptions."""
    pass

class UsernameContainsIllegalCharacter(UsernameException):
    """Exception raised when the username contains an illegal character."""
    def __init__(self, char, index):
        self.char = char
        self.index = index
        self.message = f"The username contains an illegal character '{self.char}' at index {self.index}"
        super().__init__(self.message)

class UsernameTooShort(UsernameException):
    """Exception raised when the username is too short."""
    def __init__(self):
        self.message = "The username is too short"
        super().__init__(self.message)

class UsernameTooLong(UsernameException):
    """Exception raised when the username is too long."""
    def __init__(self):
        self.message = "The username is too long"
        super().__init__(self.message)

class PasswordException(Exception):
    """Base class for password-related exceptions."""
    pass

class PasswordTooShort(PasswordException):
    """Exception raised when the password is too short."""
    def __init__(self):
        self.message = "The password is too short"
        super().__init__(self.message)

class PasswordTooLong(PasswordException):
    """Exception raised when the password is too long."""
    def __init__(self):
        self.message = "The password is too long"
        super().__init__(self.message)

class PasswordMissingCharacter(PasswordException):
    """Exception raised when the password is missing a specific character type."""
    def __str__(self):
        return "The password is missing a character"

class PasswordMissingUppercase(PasswordMissingCharacter):
    """Exception raised when the password is missing an uppercase character."""
    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    """Exception raised when the password is missing a lowercase character."""
    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    """Exception raised when the password is missing a digit."""
    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    """Exception raised when the password is missing a special character."""
    def __str__(self):
        return super().__str__() + " (Special)"

def check_input(username, password):
    """
    Checks the validity of the given username and password.

    Args:
        username (str): The username to be checked.
        password (str): The password to be checked.

    Raises:
        UsernameContainsIllegalCharacter: If the username contains illegal characters.
        UsernameTooShort: If the username is too short.
        UsernameTooLong: If the username is too long.
        PasswordMissingUppercase: If the password is missing an uppercase character.
        PasswordMissingLowercase: If the password is missing a lowercase character.
        PasswordMissingDigit: If the password is missing a digit.
        PasswordMissingSpecial: If the password is missing a special character.
        PasswordTooShort: If the password is too short.
        PasswordTooLong: If the password is too long.

    Returns:
        None

    Prints:
        "OK" if the username and password are valid.
    """
    for char in username:
        if not (char.isalnum() or char == "_"):
            raise UsernameContainsIllegalCharacter(char, username.index(char))

    if len(username) < 3:
        raise UsernameTooShort()
    elif len(username) > 16:
        raise UsernameTooLong()

    has_upper = has_lower = has_digit = has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    if not has_upper:
        raise PasswordMissingUppercase()
    elif not has_lower:
        raise PasswordMissingLowercase()
    elif not has_digit:
        raise PasswordMissingDigit()
    elif not has_special:
        raise PasswordMissingSpecial()

    if len(password) < 8:
        raise PasswordTooShort()
    elif len(password) > 40:
        raise PasswordTooLong()

    print("OK")

def main():
    """
    Prompts the user to enter a username and password until valid input is provided.
    """
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break
        except UsernameException as e:
            print(f"Username error: {e}")
            continue
        except PasswordException as e:
            print(f"Password error: {e}")
            continue
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

if __name__ == "__main__":
    main()