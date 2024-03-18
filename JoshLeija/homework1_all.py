#Module 1: Python Basics
# 1: Variables

#Create a program that prints your name on screen.
#Create two variables, name and age, and assign your name and age to these variables. Then, print a message saying "My name is [name], and I am [age] years old."
#Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print #the result.
 
#print ("Josh Leija")

#x=("Josh")
#y=("41")

#print ("My name is",x,", and I am ",y,"years old.")

#a=23.0
#b=9/5
#temperature_fahrenheit=a*b+32

#print (temperature_fahrenheit)


# 2: Operators

#Take two integers from the user and store them in variables a and b. Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus.            Note: You #can accept user input by writing name = input(“Please input your name: “)
#Given a variable x with the value 5, write a Python expression using the assignment operator (+=) to increase the value of x by 10, and then print the new value of x.

#print("Enter number 1")
#num1 = input()
#num1 = int(num1)

#print("Enter number 2")
#num2 = input()
#num2 = int(num2)

#answer1 = num1 + num2
#answer2 = num1 - num2
#answer3 = num1 * num2
#answer4 = num1 / num2
#answer5 = num1 % num2

#print(answer1, "is both numbers summed")
#print(answer2, "is the difference of both numbers")
#print(answer3, "is both numbers multiplied")
#print(answer4, "is both numbers divided")
#print(answer5, "features the result of the modulus feature")


#x=5
#x += 10
#print(x, "is the new value of x")


# 3: Lists

#Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list and remove "banana". Print the final list.
#Given a list of numbers, write a Python script to find the sum of all the numbers in the list.
 
#lst = ["apple", "banana", "cherry"]
#lst.append("orange")
#lst.remove("banana")
#print(lst)

#lst2 = [1,2,3,4,5]
#print(lst2[0]+lst2[1]+lst2[2]+lst2[3]+lst2[4])


#4: List Slicing

#Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], slice it to obtain a new list containing only the last three elements. Print the new list.
#Reverse the list numbers using slicing and print the reversed list.
 
#lst=[0,1,2,3,4,5,6,7,8,9]
#print (lst[7:10:])

#lst=[0,1,2,3,4,5,6,7,8,9]
#print (lst[-1:-4:-1])


#5: Conditional Statements 

#Write a Python script that takes an integer from the user and prints whether the number is positive, negative, or zero.
#Extend the above program to check if the number is even or odd, and print this information as well.
 
#print("Enter number")
#num = input()
#num= int(num)
#if num > 0:
#   print("Positive")
#   if (num % 2) == 0:
#       print("Even")
#   else:
#       print("Odd")
#elif num < 0:
#   print("Negative")
#   if (num % 2) == 0:
#       print("Even")
#   else:
#       print("Odd")
#else:
#   print("Zero") 

#6: For Loops

#Write a Python program using a for loop that prints all the even numbers from 1 to 50.

#for i in range(52):
#    if (i % 2) == 0:
#        print(i)

#Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1).
 
lst = ["Fred", "Barney", "Wilma", "Betty"]

#item1 = enumerate(lst)

#print (list(enumerate(lst, 1)))
#print (type(item1))

#7: While Loops

#Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". Print each word entered by the user. Warning! This is an infinite loop so take care.

#entered = []

#new =""
#while new != "quit":
#   new = input("Please enter a word ")
    
#   if new != "quit":
#       entered.append(new)
                         
#print(entered)

#Write a while loop that counts down from 10 to 1 and then prints "Success!".

#print("Countdown")
#for i in range(1,11)[::-1]:
#   print(i)
#print("Success!")

     


