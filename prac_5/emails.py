
def extract_name_from_email(email):
    username = email.split('@')[0]
    if '.' in username:
        parts = username.split('.')
        name = ' '.join(part.capitalize() for part in parts)
    elif '_' in username:
        parts = username.split('_')
        name = ' '.join(part.capitalize() for part in parts)
    else:
        name = username.capitalize()
    return name


def main():
    user_data = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation == 'n':
            name = input("Name: ").strip().title()

        user_data[email] = name

    for email, name in user_data.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
