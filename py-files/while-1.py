#while Loop
'''
while <expr>:
    <statement(s)>
'''
print("simple while")
n =10
while n > 0:
    n -= 1 #n=n-1
    print(n)
#
print("while with break")
n =10
while n > 0:
    n -= 1 #n=n-1
    print(n)
    if n==4:
        break
#
print("while with continue")
n =10
while n > 0:
    n -= 1 #n=n-1
    if n>4:
        continue
    print(n)
#The else
print("while with else")
n =10
while n > 0:
    n -= 1 #n=n-1
    print(n)
else:
    print('Loop done.')
#One-Line while Loops
print("One-Line while Loops")
n=10
while n > 0: n -= 1; print(n)
