""" 1. შემოატანინეთ მომხმარებელს თავისი ასაკი input  ფუნქციის გამოყენებით
 შემდეგ შეამოწმეთ ასაკი არის თუ არა  მეტი  ან უდრის0 და ნაკლები 18 ზე დაუბეჭდეთ
 სხვა შემთხვევაში მეტია ან უდრის18 ზე და ნაკლებია 50 ზე დავუბეჭდოთ
 რომ არის ზრდასრული სხვა შემთხვევაში ის არის მოხუცი"""


age = float(input("please enter your age: "))

if age >=0 and age <18:
    print("your are kid")
elif age <=18 and age >50:
    print("you are an adult")
else:
    print("yo are old")


"""2) მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ შემოტანილი რიცხვი,
 თუ რიცხვი მეტია ნულზე მაშინ დავუბეჭდოთ რომ რიცხვი არის დადებით,
სხვა შემთხვევაში თუ რიცხვი ნაკლებია ნნულზე დავუბეჭდოთ რომ რიცხვი არის უარყოფითი,
 ხოლო სხვა შემთხვევაში დაბეჭდეთ რომ რიცხვი არის 0"""

number = float(input("Please enter number: "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is 0")