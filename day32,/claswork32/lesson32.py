def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"

def find_difference(a, b):
    a= a[0] * a[1] * a[2]
    b= b[0] * b[1] *b[2]
    
    if a > b:
        return a - b
    else:
        return b - a

def triple_trouble(one, two, three):
    string=""
    for a in range(len(one)):
        string += one[a] + two[a] + three[a]
    return string





def arithmetic(a, b, operator):
    if operator =="add":
        return a+b
    elif operator =="subtract":
        return a-b
    elif operator =="multiply":
        return a*b
    elif operator =="divide":
        return a/b


def in_asc_order(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i -1]:
            return False
    return True


def show_sequence(n):
    if n < 0:
        return str(n) + "<0"
    elif n == 0:
        return "0=0"
    else:
        series_list = []
        for i in range(n+1):
            series_list.append(str(i))
        series = '+'.join(series_list)
        total = sum(range(n+1))
        return series + " = " + str(total)