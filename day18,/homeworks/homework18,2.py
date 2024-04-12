"""სიაში შეიტანეთ 30-იდან 50-ის ჩათვლით არსებული ყველა რიცხვი.
 შემდეგ დაითვალეთ ამ სიაში არსებული კენტი რიცხვები და დაბეჭდეთ მათი რაოდენობა."""


numbers = []

print("Enter 10 numbers:")
for i in range(10):
    number = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(number)

max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("The largest number in the list is:", max_number)