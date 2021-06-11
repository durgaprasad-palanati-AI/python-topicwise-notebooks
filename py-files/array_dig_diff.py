import math
import os
import random
import re
import sys
import math
def diagonalDifference(arr):
    # Write your code here
    size=int(math.sqrt(len(arr)))
    d1=0 #0,4,8
    d2=0 #2,4,6
    print(size)
    for i in range(0,size):
        d1=d1+arr[i*(size+1)]
        d2=d2+arr[(i+1)*(size-1)]
    print(d1,d2)
    return abs(d1-d2)     
        



arr = [1,2,-1,4,5,6,7,8,9]

result = diagonalDifference(arr)

print(result)
