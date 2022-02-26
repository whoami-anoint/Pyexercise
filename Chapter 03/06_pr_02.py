message = ''' Dear |NAME|,
Greetings from Anoint
            You are invited to candle night dinner!
              Date: |DATE|
              '''
print(message)

name = input("Enter your Name: ")
date = input("Enter Date: ")
message = message.replace("|NAME|", name)
message = message.replace("|DATE|", date)
print(message)