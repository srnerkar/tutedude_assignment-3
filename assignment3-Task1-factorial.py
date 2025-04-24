
''' This program will print the factorial of the number inserted by user '''

def factorial(num):
    fact = 1
    while num > 1 :
        fact = fact * num
        num = num - 1
    return fact

number = int(input("Enter a number : "))

print(f"Factorial of {number} is : {factorial(number)}")

