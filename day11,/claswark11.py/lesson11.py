#money = 10

#if money == 10:
#    print("hello")
#else:
#    print("bye")


"""დავალება: მომხმარებელს შემოატანინეთ input_ით ფულის რაოდენობა. თუ ის აღემატება 100_ს
მაშინ დავბეჭდოთ რომ მას გააჩნია საკმარისი თანხა, სხვა შემთხვევაში კი დავბეწდოთ რომ 
მას არ აქვს საკმარისი თანხა"""


money = float(input("How much money do you have?"))

if  money > 100:
    print("You have enough money")
else:
    print("Don't have enough money")

"""დავალება2: მომხმარებელს შეეკითხეთ საკუთარი ასაკი, თუ ის აღემატება თვრამმეტს მაშინ გამოიტანეთ რომ
ის არის სრულწლოვანი, სხვა შემთხვევაში დაბეჭდეთ რომ, ის არის ბავშვი"""

age = float(input("How old are you?"))

if age >= 18:
    print("You are an adult")
else:
    print("You are a child")