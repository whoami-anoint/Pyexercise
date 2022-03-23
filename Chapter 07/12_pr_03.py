# 03) Attempt problem 1 using while loop.

num = int(input("Enter your number: "))
i = 1 
while i in range(0,11):
    print(f"{num} X {i} = {num*i}")
    i = i + i 