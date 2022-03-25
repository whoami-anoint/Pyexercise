# 05) Write a program to calculate the factorial of a given number using for loop.

# n! = 1*2*3*4*............* n 
# 5! = 1*2*3*4*5

num = int(input("Enter the number: "))
factorial = 1 
for i in range(1,num+1):
    factorial = factorial * i 
print(f"The factorial of this number is {factorial}")


num = int(input("Enter the number: "))
factorial = 1 
for i in range(1,num+1):
    factorial = factorial * i 
print(f"The factorial of this number is {factorial}")
