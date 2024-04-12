"""1:ლუწი რიცხვები: დაწერეთ პროგრამა,
 რომელიც ბეჭდავს ყველა ლუწ რიცხვს 0-დან 20-მდე while ციკლის გამოყენებით."""

i = 0
while i <=20:
    i = i + 2
    print(i)

"""2:პაროლის შემოწმება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. 
განაგრძეთ კითხვა, სანამ სწორი პაროლი არ იქნება შეყვანილი. დავუშვათ,
 რომ სწორი პაროლი არის "12345678"."""

Password = float(input("Enter your password:"))

if Password == 12345678:
    print("password is correct")
else:
    print("wrong password, Please try again")


"""3:Timer: დაწერეთ პროგრამა, რომელიც ითვლის 10-დან 1-მდე,
 დაბეჭდავს თითოეულ რიცხვს და შემდეგ დაბეჭდავს "დრო ამოიწურა"."""


i = 0

while i <= 9:
    i = i + 1
    print(i)
print("Time's up")


"""4:შეამოწმეთ ლუწია თუ კენტი: დაწერეთ პროგრამა, 
რომელიც მომხმარებელს სთხოვს რიცხვს და ბეჭდავს ლუწია თუ კენტი."""

"""ვარიანტი 1 :""" 
number = float(input("Please enter a number from 1 to 10:"))

i = 2,4,6,8,10

if number == i:
    print(" This number Odd")
else:
    print("This number Even")

"""ვარიანტი 2 :"""


number = float(input("Please enter a number from 1 to 10:"))

while number % 2 != 0:
    print("This number Odd")
    break
else:
    print("This number Even")



