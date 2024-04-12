"""1) დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ
 დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)"""

age = float(input("please enter your age: "))

if age >=0 and age <18:
    print("your are minor")
elif age <=18 and age >65:
    print("you are an adult")
else:
    print("yo are citizen")

"""2) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ
 დაბეჭდოს რიცხვი ლუწია თუ კენტი.
 გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი."""



number = float(input("Please enter number: "))

if number % 2 != 0:
    print("This number is even")
else:
    print("This number is odd")

