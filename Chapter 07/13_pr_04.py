# 04) Write a program to find whether a given number is prime or not.

num = int(input("Enter your number: "))
prime = True 
for i in range(2,num):
    if (num%2==0):
        prime = False
        break
if prime:
    print("This number is prime.")
else:
    print("This number is not prime.")