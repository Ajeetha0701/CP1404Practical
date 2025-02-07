"""
Prompt the user to input their sales.
While the sales amount is greater than or equal to 0:
If sales are less than $1,000, calculate the bonus as 10% of the sales.
Otherwise, calculate the bonus as 15% of the sales.
Display the calculated bonus.
Prompt the user to input the next sales value.
Exit the loop if the sales amount is negative.
"""
# CODE:
sales = float(input("Enter sales: $"))
while sales >= 0:  # until get negative number
    if sales < 1000:
        bonus = sales * 10 / 100
    else:
        bonus = sales * 15 / 100
    print(bonus)
    sales = float(input("Enter sales: $"))
