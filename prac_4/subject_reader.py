"""
List program
"""
FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_data(data)
    print()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts = int(parts[2])  # Convert number of students to an integer
        print(parts)   # See if that worked
        subjects.append(parts)
    input_file.close()
    return subjects


def print_data(data):
    for subject in data:
        print(subject)


def display_subject_details(data):
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
