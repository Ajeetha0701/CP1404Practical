"""
Testing demo using assert and doctest
"""

import doctest
from Prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return (" ").join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    test_car = Car()
    assert test_car.name == ""
    assert test_car._odometer == 0
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    phrased_to_sentence("how now brown cow")
    phrased_to_sentence("How now brown cow.")


doctest.testmod()


def phrased_to_sentence(phrase=""):
    sentence = phrase.capitalize()
    if sentence[-1] != ".":
        sentence += ","
    return sentence


run_tests()
