
COLORS = {
    'ALICEBLUE': '#F0F8FF',
    'ANTIQUEWHITE': '#FAEBD7',
    'AQUA': '#00FFFF',
    'BLACK': '#000000',
    'BLUE': '#0000FF',
    'GREEN': '#008000',
    'RED': '#FF0000',
    'WHITE': '#FFFFFF',
    'YELLOW': '#FFFF00',
    'GRAY': '#808080'}


def get_color_code(color_name):
    return COLORS.get(color_name.upper())


def main():
    color_name = input("Enter a color name (blank to quit): ").strip()
    while color_name:
        color_code = get_color_code(color_name)
        if color_code:
            print(f"The hexadecimal code for {color_name.capitalize()} is {color_code}.")
        else:
            print(f"Sorry, '{color_name}' is not a valid color name.")

        color_name = input("Enter a color name (blank to quit): ").strip()


if __name__ == "__main__":
    main()

