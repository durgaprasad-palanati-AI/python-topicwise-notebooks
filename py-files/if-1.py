'''
if <expr>:
    <statement>
'''

# If the given number is positive, print an appropriate message

num = 5
if num > 0:
    print(num, "is a positive number.")

'''
if <expr>:
    <statement>
else:
    <statement>
'''
# Check given number is positive or negative, print an appropriate message
num = -2
if num > 0:
    print(num, "is a positive number.")
else:
    print(num, "is a neagtive number.")

'''
if <expr>:
    <statement>
elif <expr>:
    <statement>
else:
    <statement>
'''

#
num=0
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
