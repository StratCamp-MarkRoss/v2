# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables.
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius.
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b.
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5,
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
    total = 0
    for num in myNumberList:
        total += num
    return total

result = calculate_sum([2, 4, 6, 8])
print(result)
# 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#slice it to obtain a new list containing only the last three elements. Print the new list.

NumbersList=[0,1,2,3,4,5,6,7,8,9]
NumbersList[7:]
#OR
NumbersList[-3:]
# 1.Write a Python script that takes an integer from the user and prints whether the number is
# positive, negative, or zero.

Num= int(input("enter the number:" ))

if  Num>0:
    print('positive')
elif Num<0:
    print('negative')
else:
    print('zero')
    # 2.Extend the above program to check if the number is even or odd, and print this information as well.

Num= int(input("enter the number:" ))
if  Num>0:
    print('positive')
elif Num<0:
    print('negative')
else:
    print('zero')
if Num%2==0:
    print('even')
else:
    print('odd')
# 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

for i in range(1,51,1):   #for i in range (2,51,2) works too
    if i %2==0:
        print(i)
# 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

# List of names
Names = ["Alice", "Bob", "Charlie", "David"]

# Iterate over the list using enumerate
for i, name in enumerate(Names, start=1):
    print(f"{i}: {name}")
# 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
# Print each word entered by the user. Warning! This is an infinite loop so take care

List=[]
while True:
    word=input("Enter a word(type 'quit' to stop)")
    if word.lower=='quit':
        break
    List.append(word)
print("Words added: ")
for word in List:
    print(word)

###################### REVISE, ASK  & INQUIRE
# 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
i = 10
while i>=1:
    if i==0:
        break
    print(i)
    i-=1
print("Success!")

#OR
counter = 10
while counter >= 1:
    print(counter)
    counter -= 1
print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")
# 1.Create a program that prints your name on screen.
name='Ali Lawati'
print(name)
# 2.Create two variables, name and age, and assign your name and age to these variables. 
#Then, print a message saying "My name is [name], and I am [age] years old."
name='Ali Lawati'
age=30
print('My name is',name,'and I am',age, 'years old')
# 3.Define a variable temperature and assign a float value to it to represent the current temperature in Celsius. 
#Convert this temperature to Fahrenheit and store the result in a variable temperature_fahrenheit. Print the result.

celsius_temp=25.0
temperature_fahrenheit=(celsius_temp*(9/5))+32
print('temperature_fahrenheit is',temperature_fahrenheit)
# 1.Take two integers from the user and store them in variables a and b. 
#Perform and print the results for the following operations: addition, subtraction, multiplication, division, and modulus
#Note: You can accept user input by writing name = input(“Please input your name: “)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

Addition=a+b
print(Addition)
Subtraction=a-b
print(Subtraction)
Muliplication=a*b
print(Muliplication)
Division=a/b
print(Division)
Modulus=a%b
print(Modulus)
# 2.Given a variable x with the value 5, 
#write a Python expression using the assignment operator (+=) to increase the value of x by 10,
#and then print the new value of x

x=5
x+=10
print(x)
# 1.Create a list named fruits containing the following items: "apple", "banana", "cherry". Add "orange" to the list 
#and remove "banana". Print the final list
myList=["apple","banana","cherry"]
myList.append("orange")
myList.remove("banana")
myList
def calculate_sum(myNumberList):
        total = 0
            for num in myNumberList:
                        total += num
                            return total

                        result = calculate_sum([2, 4, 6, 8])
                        print(result)
                        # 1.Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        #slice it to obtain a new list containing only the last three elements. Print the new list.

                        NumbersList=[0,1,2,3,4,5,6,7,8,9]
                        NumbersList[7:]
                        #OR
                        NumbersList[-3:]
                        # 1.Write a Python script that takes an integer from the user and prints whether the number is 
                        # positive, negative, or zero.

                        Num= int(input("enter the number:" ))

                        if  Num>0:
                                print('positive')
                            elif Num<0:
                                    print('negative')
                                else:
                                        print('zero')
                                        # 2.Extend the above program to check if the number is even or odd, and print this information as well.

                                        Num= int(input("enter the number:" ))
                                        if  Num>0:
                                                print('positive')
                                            elif Num<0:
                                                    print('negative')
                                                else:
                                                        print('zero')
                                                        if Num%2==0:
                                                                print('even')
                                                            else:
                                                                    print('odd')
                                                                # 1.Write a Python program using a for loop that prints all the even numbers from 1 to 50.

                                                                for i in range(1,51,1):   #for i in range (2,51,2) works too
                                                                        if i %2==0:
                                                                                    print(i)
                                                                            # 2.Given a list of names, write a for loop to print each name preceded by the number of the iteration (starting with 1)

                                                                            # List of names
                                                                            Names = ["Alice", "Bob", "Charlie", "David"]

                                                                            # Iterate over the list using enumerate
                                                                            for i, name in enumerate(Names, start=1):
                                                                                    print(f"{i}: {name}")
                                                                                # 1.Implement a Python script using a while loop that asks the user to enter a word and stops asking when the user types "quit". 
                                                                                # Print each word entered by the user. Warning! This is an infinite loop so take care

                                                                                List=[]
                                                                                while True:
                                                                                        word=input("Enter a word(type 'quit' to stop)")
                                                                                            if word.lower=='quit':
                                                                                                        break
                                                                                                        List.append(word)
                                                                                                        print("Words added: ")
                                                                                                        for word in List:
                                                                                                                print(word)

                                                                                                                ###################### REVISE, ASK  & INQUIRE
                                                                                                                # 2. Write a while loop that counts down from 10 to 1 and then prints "Success!".
                                                                                                                i = 10
                                                                                                                while i>=1:
                                                                                                                        if i==0:
                                                                                                                                    break
                                                                                                                                    print(i)
                                                                                                                                        i-=1
                                                                                                                                        print("Success!")
                                                                                                                                          
                                                                                                                                          #OR
                                                                                                                                          counter = 10
                                                                                                                                          while counter >= 1:
                                                                                                                                                  print(counter)
                                                                                                                                                      counter -= 1
                                                                                                                                                      print("Success!")

