# 1) What are some identifying characteristics of a tuple?
# -Iterability, ordered, immutable# 2) Create a list of tuples, only numbers, like so: [(), (), ()]. 
# Have python figure out which tuple has the highest sum.

mytuplelist=[(4,4,4),(5,5,5),(6,6,6)]

highest_sum = float('-inf')  
tuple_with_highest_sum = None

for tup in mytuplelist:
     current_sum = sum(tup)

if current_sum>highest_sum:
    highest_sum=current_sum
    tuple_with_highest_sum=tup
    print(tup)# 1) What are some identifying characteristics of a set?

# -Unordered (no index), - no duplicates, - Iterable, immutable# 2) Say you have a list with the values [1, 2, 3, 3, 4, 1]. 
# How would you handle this if you wanted only unique values in the list?

mylist=[1,2,3,3,4,1]
mySet=set(mylist)
mylist=list(mySet)
print(mylist)# 3) Find the common elements between 3 sets that you have defined.
set1={9,5,0,8,6,7}
set2={9,6,3,5,2,1}
set3={5,8,6,3,7,0}

print("The common elements are:",set1 & set2 & set3)

# or

common_elements=set1.intersection(set2&set3)
print("The common elements are:",common_elements)# 1) What are some identifying characteristics of a dictionary
# - mutable, - iterbale, - unique# 2) Create two dictionaries that have user:age as the key:value pairings. Merge the two into a single dictionary.

dict1={'John':32,'Mike':34}
dict2={'Raymond':36,'William':30}

dict1.update(dict2)
print(dict1)

# OR
combined_dict={**dict1,**dict2}
print(combined_dict)# 3) Create a dictionary. Remove an entry. Add an entry.
my_dict={'name':'Jane','age':35,'employer':'Tesla'}
print(my_dict)
my_dict.pop('employer')
print(my_dict)
my_dict.update({'University':'MIT'})
print(my_dict)# 1) Accept a user input string into a variable. Print the string back but replace all vowels with “*”.

myinput=input("Add your input: ")
vowels='a,e,i,o,u,A,E,I,O,U'
result= ''
for char in myinput:
    if char in vowels:
        result+="*"
    else:
        result+=char
print(result)# 2) Accept a user input string into a variable. Print the string back, backwards.

userinput=input("Enter your input: ")
print(userinput[::-1])# 3) Accept a user input string into a variable. If the input looks like a valid email address, print “True”. 
# If not, print “False”

email=input('please enter your email address: ')
parts = email.split('@')
result=''
if len(parts)==2:
    result='True'
else:
    result='false'
print(result)# 4) Accept four user-inputted values: Name, Age, City, and Phone. 
# Print back the following sentence: 
# “Your name is [Name], and you are [Age] years old. You live in [City], and your phone number is [Phone].”


Name=input('Enter your name: ')
Age=input('Enter your age: ')
Citi=input('Which city you live? ')
Phone=input('Add your contact number: ')

print(f'Your name is {Name}, and you are {Age} years old. You live in {Citi}, and your phone number is {Phone}')
