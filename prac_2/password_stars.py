# CODE:


def get_password():
    """
    Prompt the user to enter a password and return it.
    """
    password = input("Enter your password: ")
    return password


def print_password_asterisks(password):
    """
    Print asterisks corresponding to the length of the password
    param password: The password whose length determines the number of asterisks to print.
    """
    print('*' * len(password))


def main():
    """
    Main function to execute the password check program.
    """
    password = get_password()
    print_password_asterisks(password)


if __name__ == "__main__":
    main()




