"""2) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ
 დაბეჭდოს რიცხვი ლუწია თუ კენტი.
 გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი."""



number = float(input("Please enter number: "))

if number % 2 != 0:
    print("This number is odd")
else:
    print("This number is even")
