"""
LIST COMPREHENSIONS
"""
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# List comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# List comprehension to create a list of integers from the above list of strings
numbers = [int(num) for num in almost_numbers]
print(numbers)

greater_than_9 = [num for num in numbers if num > 9]
print(greater_than_9)

# Use a list comprehension and the join string method to create a string (not list) of the last names
# for those full names longer than 11 characters
long_last_names = [name.split()[1] for name in full_names if len(name) > 11]
print(", ".join(long_last_names))





