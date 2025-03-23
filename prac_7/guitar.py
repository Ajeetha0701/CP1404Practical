class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, {self.year}, ${self.cost:,.2f}"

    def get_age(self, current_year=2024):
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year


def read_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name = data[0].strip()
            year = int(data[1].strip())
            cost = float(data[2].strip())
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def main():
    guitars = read_guitars("guitars.txt")

    print("Guitars:")
    display_guitars(guitars)

    guitars.sort()

    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)


if __name__ == "__main__":
    main()
