
# Data Structures list, string, tuple
numbers = [1, 2, 3, 6, 5]
numbers = [x for x in range(6) if x < 10]

more_numbers = [6, 7]
pangram = 'The quick brown fox jumps over the lazy dog'
pairs = (1, 2)
singular = (3, )

# Common functions on all the above Data Structures.

# 1 Slicing. Format a[from:to:step]
reversed_panagram = pangram[::-1]

# 2 Concatenation/Adding
triplets = pairs + singular
numbers = numbers + more_numbers

# Lists are mutabe, Tuples are not. Members inside a Tuple can be mutable. Tuples are more efficient than lists.
# Paranthesis in tuple are optional

# 3 Check membership
check_in_list = 'The' in pangram

# 4 Iteration
for item in numbers:
    pass

for index, value in enumerate(pangram):
    pass

# 5 Length
number_of_items = len(pangram)

# 6 To implment Minimum, Maximum, Add items must be of same numeric type.
highest = max(numbers)
lowest = min(pairs)
add = sum(numbers[:5])

# 7 Count of an item
number_of_a = pangram.count('a')

# 8 Index of the first occuring item
index_of_a = pangram.index('a')

# 9 Unpacking: Match the number of items in list, tuples or strings
one, two = pairs


# Specific List functions

# Delete list[index]
del numbers[0]
# Add an item to list
numbers.append(0)

# Add a list to another list
numbers.extend(more_numbers)

# Insert item in a list to a specific index
numbers.insert(0, 10)

# Pop last item
numbers.pop()

# Remove a specified item, gives error if number not in list.
numbers.remove(6)

# Reverse a list
numbers.reverse()

# Sort a list
numbers.sort()

number = 5
number2 = 5

print(id(number))
print(id(number2))
