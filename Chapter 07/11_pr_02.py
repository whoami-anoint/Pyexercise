# 2) Write a program to greet all the person names stored in a list L1 and which stands with S.

l1 = ["Sareeta", "Sushant", "Sarmila", "Sanju", "Abhishek","Priyanka"]

for name in l1:
    if name.startswith("S"):
        print("Hello" + " "+ name)