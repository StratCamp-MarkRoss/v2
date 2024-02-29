#1: Tuples
#1)What are some identifying characteristics of a tuple?

# They are immutable and ordered, meaning you can’t modify its contents (add, remove, or change elements). They are contained within parentheses and can have different data types like integers and strings.

#2)Create a list of tuples, only numbers, like so: [(), (), ()]. Have python figure out which tuple has the highest sum. 

list_of_tuples_nums_only = ([1,2,3] , [4,5,6] , [7,8,9])
max_sum_tuple_list = max( list_of_tuples_nums_only, key=sum )

print(max_sum_tuple_list)
print(sum(max_sum_tuple_list))

#2: Sets

#1)What are some identifying characteristics of a set?

#They are mutable, unordered and unique. They are good for creating uniqueness, and to do mathematical operations. They are contained within curly braces,  and do not allow for duplicate elements.

#2)Say you have a list with the values [1, 2, 3, 3, 4, 1]. How would you handle this if you wanted only unique values in the list?

# I would handle this by turning the list of values into a set:

my_list = [1, 2, 3, 3, 4, 1]
print(my_list)

my_set = set(my_list)
print(my_set)

#3)Find the common elements between 3 sets that you have defined.

set1 = {1 , 2 , 3 , 4}
set2 = {1 , 8 , 4 , 9}
set3 = {1 , 5 , 6 , 7}
common_elements = set1.intersection(set2, set3)
print("Common Elements:", common_elements)

#3: Dictionaries

# 1) What are some identifying characteristics of a dictionary
# Dictionaries are key value pairs , unordered, and are mutable. They are contained within curly braces similar to sets but the key-value pairs are separated by a colon (“:”)  in dictionaries. 

# 2) Create two dictionaries that have user:age as the key:value pairings. Merge the two into a single dictionary.
dictionary1 = { "Gurk" : 29 , "Jasleen" : 28 } 
dictionary2 = { "Kato" : 5 , "Amy" : 25 }

dictionary3 = {**dictionary1, **dictionary2}
print("Combined Dictionary:", dictionary3)

#3) Create a dictionary. Remove an entry. Add an entry.
dictionary4 = { "name" : "Gurk" , "age" : 29 , "fave number" : 11}

#Adding entry
dictionary4["Job"] = "Banking"
print(dictionary4)

#Removing entry
del dictionary4["age"]
print(dictionary4)


# 4: Strings

#1) Accept a user input string into a variable. Print the string back but replace all vowels with “*”.
user_input = str(input("Enter a string: "))

vowel_replacement = ""
for x in user_input:
    if x.lower() in "aeiou":
        vowel_replacement += "*"
    else:
        vowel_replacement += x
print(vowel_replacement)

# 2) Accept a user input string into a variable. Print the string back, backwards.
user_input = str(input("Enter a string: "))
reverse_input = user_input[::-1]
print(reverse_input)

# 3) Accept a user input string into a variable. If the input looks like a valid email address, print “True”. If not, print “False”
user_input = str(input("Enter a string: "))
if '@' in user_input and '.' in user_input:
    print("Is Valid Email: True")
else:
    print("Is Valid Email: False")

#4) Accept four user-inputted values: Name, Age, City, and Phone. Print back the following sentence: “Your name is [Name], and you are [Age] years old. You live in [City], and your phone number is [Phone].”

Name = str(input("Enter your name: "))
Age = str(input("Enter your age: "))
City = str(input("Enter your city: "))
Phone = str(input("Enter your phone: "))

sentence = f"Your name is {name}, and you are {age} years old. You live in {city}, and your phone number is {phone}.”
print(sentence)

