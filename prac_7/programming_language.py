class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, pointer_arithmetic, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, " \
               f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def __lt__(self, other):
        return self.year < other.year


def read_programming_languages(filename):
    languages = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name = data[0].strip()
            typing = data[1].strip()
            reflection = data[2].strip() == 'True'
            pointer_arithmetic = data[3].strip() == 'True'
            year = int(data[4].strip())
            languages.append(ProgrammingLanguage(name, typing, reflection, pointer_arithmetic, year))
    return languages


def display_programming_languages(languages):
    for language in languages:
        print(language)


def main():
    languages = read_programming_languages("programming_languages.txt")

    print("Programming Languages:")
    display_programming_languages(languages)

    languages.sort()

    print("\nProgramming Languages sorted by year (oldest to newest):")
    display_programming_languages(languages)


if __name__ == "__main__":
    main()
