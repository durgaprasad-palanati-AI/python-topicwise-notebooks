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

#One-Line if Statements
num=4
if num==4: print('1'); print('2'); print('3')

#Conditional Expressions (Python’s Ternary Operator)
'''
<expr1> if <conditional_expr> else <expr2>
'''
num=9
number_is='even' if num%2==0 else 'odd'
print(number_is)

#The Python pass Statement
'''
if <expr>:
    pass
'''

num=10
if num==10:
    pass #if you remove this line error occurs
