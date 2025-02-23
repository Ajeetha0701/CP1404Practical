import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PICKS = 6
NUM_QUICK_PICKS = int(input("How many quick picks? "))


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks <= 0:
        print("Invalid input!")
        quick_picks = int(input("How many quick picks? "))

    for column in range(quick_picks):
        quick_pick = []
        for row in range(NUM_PICKS):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()


