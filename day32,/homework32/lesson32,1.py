def no_odds(values):
    a=[]
    for i in values:
        if i %2 ==0:
            a.append(i)
    return(a)

def sum_cubes(n):
    total=0
    for i in range(1,n+1):
        total += i**3
    return total

def number_of_occurrences(element, sample):
    total=0
    for i in sample:
        if i == element:
            total+=1
    return total

