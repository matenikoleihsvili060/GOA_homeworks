#1) 
from math import *

def litres(time):
    return floor (time * 0.5)

#მეორე ხერხი
def litres (time):
    return int(time * 0.5)

#მესამე ხერხი
def litres (time):
    return time * 0.5 // 2

#2)
def paperwork(n,m):
    if n < 0 or m < 0:
        return 0
    
    return n * m

#3)
def grow(numbers_list):
    result = 1
    
    for number in numbers_list:
        result = result * number
    
    return result

#4)
def grow(numbers_list):
    result = 1
    
    for number in numbers_list:
        result = result * number
    
    return result

#5)
def count_by(x, n):
    multiples_x = []
    
    for i in range(x, x * n + 1):
        if i % x == 0:
            multiples_x.append(i)
    
    return multiples_x
#მეორე ხერხი
def count_by(x, n):
    return list(range(x, x * n + 1, x))
