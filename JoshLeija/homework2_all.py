#Module 2, Section 1 (Tuples)
#Question 1: What are some identifying characteristics of a tuple?
#Answer: They are immutable and ordered.

#Question 2: Create a list of tuples, only numbers, like so: [(), (), ()]. Have python figure out which tuple has the highest sum.
#tuples_list = [(1), (2), (3), (4)]
#y = max(tuples_list)
#print(y)

#Module 2, Section 2 (Sets)
#Question 1: What are some identifying characteristics of a set?
#Answer: They are mutable, unordered, and unique.

#Question 2: Say you have a list with the values [1, 2, 3, 3, 4, 1]. How would you handle this if you wanted only unique values in the list?
#Answer: Just by putting it in a set with these brackets {}, the output will show only unique numbers. You could also use the discard command to get rid of extra values.

#Question 3: Find the common elements between 3 sets that you have defined.
#a = {1,2,3,4}
#b = {2,4,6,8}
#c = {2,4,8,16}
#print(a&b&c)

#Module 2, Section 3 (Dictionaries)
#Question 1: What are some identifying characteristics of a dictionary?
#Answer: They are mutable key-value pairs.

#Question 2:  Create two dictionaries that have user:age as the key:value. Merge the two into a single dictionary.
#student1 = {"Name": "John", "Age": 20}
#student2 = {"Name2": "Mike", "Age2": 22}

#merged_students = { **student1, **student2}
#print(merged_students)

#Question 3: Create a dictionary. Remove an entry. Add an entry.

#student1 = {"Name": "John", "Age": 20}
#del student1["Age"]
#print(student1) 

#student1 = {"Name": "John", "Age": 20}
#student1["City"]="New York"
#print(student1) 

#Module 2, Section 4 (Strings)
#Question #1: Accept a user input string into a variable. Print the string back but replace all vowels with “*”.

#input_string = input("enter a word ")
#vowels = "aeiouAEIOU"
#vowel_count = sum(1 for char in input_string if char in vowels)

#vowels_only = ""
#vowels_only = vowels_only.join(char for char in input_string if char in vowels)

#print(vowels_only)


#Question #2:  Accept a user input string into a variable. Print the string back, backwards.


#input_string = input("enter a word ")

#for char in input_string[::-1]:

#    print(char)


#Question #3:  Accept a user input string into a variable. If the input looks like a valid email address, print “True”. If not, print “False”

#input_string = input("enter an email: ")

#if input_string.count("@") == 1 and input_string.count(".") == 1:
#    print("True")
#else:
#    print("False")




#Question #4:   Accept four user-inputted values: Name, Age, City, and Phone. Print back the following sentence: “Your name is [Name], and you are [Age] years old. You live in [City], and your phone number is [Phone].”
#name = input("Enter your name ")
#age = input("Enter your age ")
#city = input("Enter your city ")
#phone = input("Enter your phone ")

#print(f"Your name is {name}, and you are {age} years old. You live in {city}, and your phone number is {phone}.")

