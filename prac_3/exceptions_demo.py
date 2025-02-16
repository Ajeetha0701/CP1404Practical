"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: It will occur when the user inputs a vale that cannot
        be converted to an integer using the "int()" function.
2. When will a ZeroDivisionError occur?
Answer: It will occur when the user inputs a denominator of zero as division
        by zero is mathematically undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: yes you can add a conditional check to ensure that the
        denominator is not zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
