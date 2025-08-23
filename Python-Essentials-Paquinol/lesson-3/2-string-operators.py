# String Operators
# + concatenation, * repetition

first_name = "John"
last_name = "Doe"

# full_name = first_name + " " + last_name

full_name = first_name + " " + last_name
print(full_name)

# string repetition

word = "Hello\n"
# repeat the word 3 times
repeated_word = word * 3
print(repeated_word)

# string comparison or relational operators ("==", "!=", ">", "<", ">=", "<=")

fruit1 = "apple"
fruit2 = "banana"

print(fruit1 == fruit2) # False
print(fruit1 != fruit2) # True
print(fruit1 > fruit2) # False
print(fruit1 < fruit2) # True
print(fruit1 >= fruit2) # False
print(fruit1 <= fruit2) # True

# it compares strings alphabetically (a-z)
# "apple" is less than "banana" because "a" is less than "b" it uses the ASCII values of the characters
# ASCII values are the numerical values of the characters
# A-Z = 65-90, a-z = 97-122


# string membership operators ("in", "not in")
sentence = "The ferson is a good boy"
print("son" in sentence) # True
print("son" not in sentence) # False because fer"son" is in the sentence
print("son" in sentence.lower()) # True because "son" is in the sentence in lowercase
print("giraffe" in sentence) # False because "giraffe" is not in the sentence

# string identity operators ("is", "is not")

x = 10
y = 10
z = 20
print(x is y) # True
print(x is not z) # True

# string slicing or indexing
text = "Hello World" # 0-10
print(text[0]) # H
print(text[1]) # e
print(text[2]) # l
print(text[3]) # l
print(text[4]) # o
print(text[5]) # space
print(text[6]) # W
print(text[7]) # o
print(text[8]) # r
print(text[9]) # l

extracted_string = text[0:5] # Hello 
# the first ["starting index":] is the start index and the second [:"end index"] is the end index
print(extracted_string)
