print("Dhruv Angle")
Name = "Dhruv Angle"
Age = 25
print("My name is {}, and I am {} years old today.".format(Name, Age))
Temperature = 33.2
Temperature_fahrenheit = (Temperature *(9/5))+ 32
print(Temperature_fahrenheit) 
a = int(input("Please input your first integer:"))
b = int(input("Please input your second integer:")) 
Addition_result = a + b
Subtraction_result = a - b
Multiplication_result = a*b
Division_result = a/b
Modulus_result = a%b
print(Addition_result)
print(Subtraction_result)
print(Multiplication_result)
print(Division_result)
print(Modulus_result)
x=5
x+=10
print("New value of x:",x)
Fruits = [ "apple", "banana", "cherry"]
Fruits .append("Orange")
Fruits .remove("banana")
print(Fruits)
Numbers = [1,2,3,4,5,6]
sum_of_numbers = sum(Numbers)
print(sum_of_numbers)
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 =lst[7::1]
print(lst2)
lst3 = lst[::-1]
print(lst3)
number = int(input("please input integer:"))
if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")
if number % 2 ==0:
    print("the Number is even")
else:
    print("the number is odd")
for number in range (1,51):
    if number % 2 ==0:
        print(number)
Names = ["Dhruv", "Mark", "Ross", "Angle"]
iteration_number = 1
for name in Names:
    print("{}. {}".format(iteration_number , name))
    iteration_number += 1
number = 10
while number >= 1:
    print(number)
    number-= 1
print("success")
words = []
word = input("Please enter a word (or type 'quit' to exit): ")
while word != "quit":
    words.append(word)
    word = input("Please enter another word (or type 'quit' to exit): ")
print("Words entered by the user:")
for word in words:
    print(word)

