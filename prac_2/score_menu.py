"""
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50

MENU = (G)et a valid score
(P)rint result
(S)how stars
(Q)uit

"""
# CODE:


def get_valid_score():
    valid_score = False
    while valid_score:
        score_input = input("Enter a score (0-100): ")
        if score_input:
            score = float(score_input)
            if 0 <= score <= 100:
                valid_score = True
            else:
                print("Score must be between 0 and 100 inclusive.")
        else:
            print("Invalid input. Please enter a valid number.")
    return valid_score


def print_result(score_value):
    if score_value >= 90:
        print("Excellent")
    elif score_value >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score_value):
    print("*" * int(score_value))


def main():
    score = get_valid_score()
    choice = ''
    while choice != "Q":
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using the Score Program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

