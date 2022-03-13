#  Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter the username: ")
character = (username.__len__())
if character< 10:
    print("Username contains less than 10 characters")
else: 
    print("Username contains not less than 10 characters")
    