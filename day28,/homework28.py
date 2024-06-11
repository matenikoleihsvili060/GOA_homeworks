def get_average(marks):
    sam=sum(marks)
    count=len(marks)
    return sam // count


def make_negative( number ):
    if number >0:
        return -number
    else:
        return number



def str_count(strng, letter):
    return strng.count(letter)


def is_leap_year(year):
    if year % 400 ==0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 ==0:
        return True
    else:
        return False


def best_friend(txt, a, b):
    return txt.count(a)==txt.count(a+b)




