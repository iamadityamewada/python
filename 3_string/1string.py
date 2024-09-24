str = "adityamewada"
# print(str[0: :2])
#slice # str[start:end:space]

## function of string 

# 1 len return the length of string 
# print(len(str))

# endswith return true or false when string start with particular string 
# print(str.endswith("ada"))

# startswith return true of false when string start with particular given string 
# print(str.startswith("adi"))

# Define a sample string for demonstration
sample_string = "  Hello Python World  "
sample_list = ['a', 'b', 'c']

# 1. lower(): Converts all characters in the string to lowercase
lowercase_string = sample_string.lower()
print(f"lower(): {lowercase_string}")  # Output: '  hello python world  '

# 2. upper(): Converts all characters in the string to uppercase
uppercase_string = sample_string.upper()
print(f"upper(): {uppercase_string}")  # Output: '  HELLO PYTHON WORLD  '

# 3. strip(): Removes leading and trailing whitespace
stripped_string = sample_string.strip()
print(f"strip(): {stripped_string}")  # Output: 'Hello Python World'

# 4. replace(old, new): Replaces occurrences of 'Python' with 'Java'
replaced_string = sample_string.replace("Python", "Java")
print(f"replace(): {replaced_string}")  # Output: '  Hello Java World  '

# 5. split(separator): Splits the string into a list based on spaces (default separator)
split_string = sample_string.split()
print(f"split(): {split_string}")  # Output: ['Hello', 'Python', 'World']

# 6. join(iterable): Joins elements of a list using '-' as a separator
joined_string = "-".join(sample_list)
print(f"join(): {joined_string}")  # Output: 'a-b-c'

# 7. find(substring): Finds the index of the first occurrence of 'Python'
index_of_python = sample_string.find("Python")
print(f"find(): {index_of_python}")  # Output: 8

# 8. startswith(prefix): Checks if the string starts with '  Hello'
starts_with_hello = sample_string.startswith("  Hello")
print(f"startswith(): {starts_with_hello}")  # Output: True

# 9. endswith(suffix): Checks if the string ends with 'World  '
ends_with_world = sample_string.endswith("World  ")
print(f"endswith(): {ends_with_world}")  # Output: True

# 10. len(): Returns the length of the string
length_of_string = len(sample_string)
print(f"len(): {length_of_string}")  # Output: 21

'''
Explanation:
lower(): Converts all characters in the string to lowercase.
upper(): Converts all characters in the string to uppercase.
strip(): Removes leading and trailing whitespace.
replace(): Replaces a substring ('Python') with another ('Java').
split(): Splits the string into a list of words.
join(): Joins a list of strings into a single string with a specified separator (-).
find(): Returns the index of the first occurrence of 'Python'.
startswith(): Checks if the string starts with ' Hello'.
endswith(): Checks if the string ends with 'World '.
len(): Returns the total length of the string, including spaces.
'''

