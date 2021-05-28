l=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]

n = 8
   
# using list comprehension 
x = [l[i:i + n] for i in range(0, len(l), n)]
print(x)

n=4
for e in x:
    xt = [tuple(e[i:i + n]) for i in range(0, len(e), n)]
    print(xt)
