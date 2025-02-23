def read_data(filename):

    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            line = line.strip().split(",")
            data.append(line)
    return data


def get_champions(data):

    champions = {}
    for entry in data:
        champion = entry[2]
        champions[champion] = champions.get(champion, 0) + 1
    return champions


def get_countries(data):

    countries = set()
    for entry in data:
        country = entry[1]
        countries.add(country)
    return sorted(countries)


def display_champions(champions):

    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion} {wins}")


def display_countries(countries):

    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))


def main():
    filename = "wimbledon_champions"
