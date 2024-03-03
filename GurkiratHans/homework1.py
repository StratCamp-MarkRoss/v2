# 1. Create a program that prints your name on screen.
print('Gurkirat Hans')

# 2. Create two variables, name and age, and assign your name and age to these variables. Then, print a message saying "My name is [name], and I am [age] years old."
name = 'Gurkirat Hans'
age = '29' 
#Decided to leave age as a string
print("My name is " + name + " and I am " + age)

# 3. Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.
temperature = 3.889
temperature_fahrenheit = temperature * 1.8 + 32
print (temperature_fahrenheit)

# 1. Take two integers from the user and store them in variables a and b. Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus. Note: You can accept user input by writing name = input(“Please input your name: “)
# Taking input from the user
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
# Performing operations
addition_result = a + b
subtraction_result = a - b
multiplication_result = a * b

# Checking if b is not 0 for division and modulus
if b != 0:
    division_result = a / b
    modulus_result = a % b
else:
    division_result = "Cannot divide by zero"
    modulus_result = "Cannot divide by zero"

# Printing results
print(f"Addition: {addition_result}")
print(f"Subtraction: {subtraction_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}")
print(f"Modulus: {modulus_result}")

# 2. Given a variable x with the value 5, write a Python expression using the assignment operator (+=) to increase the value of x by 10, and then print the new value of x.
# Given variable x with the value 5
x = 5

# Using the assignment operator to increase the value of x by 10
x += 10

# Printing the new value of x
print(x)

# 1. Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list and remove "banana". Print the final list.
fruits = ['apple' , 'banana' , 'cherry']
print(fruits)
fruits.append('orange')
fruits.remove('banana')
print(fruits)

# 2. Given a list of numbers, write a Python script to find the sum of all the numbers in the list.
numberlist= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_numberlist = sum(numberlist)
print(sum_of_numberlist)

# 1.  Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], slice it to obtain a new list containing only the last three elements. Print the new list.
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list= numbers_list[-3:]
print(new_list)

# 2. Reverse the list numbers using slicing and print the reversed list.
numbers_list_reversed = numbers_list[::-1]

print(numbers_list_reversed)

# 1.  Write a Python script that takes an integer from the user and prints whether the number is positive, negative, or zero.
x = 0

if x > 0:
    print('positive')
elif x < 0:
    print('negative')
elif x == 0:
    print('zero')

y = int(input("Enter an integer: "))

if y > 0:
    print('positive')
elif y < 0:
    print('negative')
elif y == 0:
    print('zero')

# 2. Extend the above program to check if the number is even or odd, and print this information as well.
if y % 2 == 0:
    print('even')
else:
    print('odd')

# 1.  Write a Python program using a for loop that prints all the even numbers from 1 to 50.
for num in range(51):
    if num % 2 == 0:
        print(num)

# 2. Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1).
names_list = ['Gurk' , 'Jasleen' , 'Kato' , 'Amy']
z=1

for name in names_list:
    print(str(z) + ('.'))
    print(name)
    z += 1

names_list2 = ['Gurk' , 'Jasleen' , 'Kato' , 'Amy']
c=1
for name in names_list2:
    print(f"{c}. {name}")
    c += 1

# 1.  Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". Print each word entered by the user. Warning! This is an infinite loop so take care.
while True:
    word = input("Enter a word (type 'quit' to exit): ")

    if word.lower() == 'quit':
        break

    print("You entered:", word)

# 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
counter = 10 

while counter < 11 and counter > 0:
    print(counter)
    counter += -1 
    
print('Success!')

counter2 = 10

while counter2 >= 1:
    print(counter2)
    counter2 -= 1

print('Success!')


