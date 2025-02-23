"""
Time estimate: 15 minutes
"""


def count_word_occurrences(text):
    word_counts = {}

    # Split the text into words
    words = text.split()

    # Count occurrences of each word
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_word_counts(word_counts):
    max_word_length = max(len(word) for word in word_counts)

    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


def main():
    user_input = input("Enter a string: ")
    word_counts = count_word_occurrences(user_input)
    print_word_counts(word_counts)


if __name__ == "__main__":
    main()
