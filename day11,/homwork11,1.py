"""რიცხვის გამოცნობა: დაწერეთ პროგრამა,
რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი (მაგ., 5, ეს რიცხვი თქვენ აირჩიეთ). 
განაგრძეთ კითხვა, სანამ არ გამოიცნობენ სწორად."""

number = float(input("Please enter a number from 1 to 10:"))

if number == 5:
    print("You won")
else:
    print("You lost,  Please try again")


"""სახელის გამოცნობა. შექმენით ცვლადი სადაც იქნება შენახული თქვენი სახელი.
მომხმარებელს შეეკითხეთ სახელი და სანამ თქვენსას არ შემოიტანს თავიდან შეეკითხეთ. """

name = (input("Write a name"))

if name == "mate":
    print("That's right")
else:
    print("This answer is incorrect, please try again") 

   



