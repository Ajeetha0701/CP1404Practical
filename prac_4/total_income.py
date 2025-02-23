def get_monthly_incomes(num_months):
    incomes = []

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1,  num_months + 1):
        total += incomes[month - 1]
        total += incomes
        print(f"Month {month:2} - Income: ${incomes:10.2f} Total: ${total:10.2f}")


def main():
    """Display income report for incomes over a given number of months."""
    num_months = int(input("How many months? "))
    monthly_incomes = get_monthly_incomes(num_months)
    print_income_report(monthly_incomes)


if __name__ == "__main__":
    main()
