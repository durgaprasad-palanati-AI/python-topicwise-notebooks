#Collection-Based or Iterator-Based Loop
'''
for i in <collection>
    <loop body>
'''

# List of numbers
numbers = [10,20,30,40,50]

for num in numbers:
    print(num)

# variable to store the sum
sum = 0

# iterate over the list
for num in numbers:
    sum = sum+num

print("The sum is", sum)

#for loop with else
print("#for loop with else")
for num in numbers:
    print(num)
else:
    print("No items left.")

#break keyword
print("#break keyword")
for num in numbers:
    if num<30:
        print(num)
        break
#with no break keyword
print("#no break keyword")
for num in numbers:
    if num<30:
        print(num)

#continue keyword
print("#continue keyword")
for num in numbers:
    if num==30:
        continue
    print(num)
        

