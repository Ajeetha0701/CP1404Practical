"""

"""
# CODE:
import random


def get_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def main():
    user_score = float(input("Enter score: "))
    print("User's result:", end=" ")
    get_result(user_score)

    # Generating a random score
    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    print("Random result:", end=" ")
    get_result(random_score)


if __name__ == "__main__":
    main()

