"""3) დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები
 ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
If the grade is A, print "Excellent!"
If the grade is B, print "Good job!"
If the grade is C, print "You passed."
If the grade is D, print "You can do better."
If the grade is F, print "You failed."""

scor = input("Enter the score (A, B, C, D ან F): ")

if scor == 'a':
    print("Excellent!")
elif scor == 'b':
    print("Good job!")
elif scor == 'c':
    print("You passed.")
elif scor == 'd':
    print("You can do better.")
else:
    print("You failed.")
