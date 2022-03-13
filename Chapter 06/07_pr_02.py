'''
Write a program to find out whether a student is pass or fail,
if it requires total 40% and at least 33% in each subject to pass.
3 subjects and take marks as an input from the user.
'''

sub1 = int(input("Enter first subject: "))
sub2 = int(input("Enter second subject: "))
sub3 = int(input("Enter third subject: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of subjects ")

elif(sub1+sub2+sub3)/3 <40:
    print("You are fail do to total percentage is less than 40")

else: 
    print("Congratulation! You are passed the exam.")