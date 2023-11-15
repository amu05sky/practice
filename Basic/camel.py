def camelcase(st):
    word_count = 1  # Initialize the word count to 1 for the first lowercase word
    for char in st:
        # Increment the word count for every uppercase letter encountered
        if char.isupper():
            word_count += 1
    return word_count

# Reading input from the user
s = input("Enter the CamelCase string: ")

# Calling the function and printing the result
result = camelcase(s)
print("Number of words in the string:", result)
# I/p: saveChangesInTheEditor
# O/p: 5