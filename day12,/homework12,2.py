"""დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი.
 მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა, 
 რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა.
 თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision"."""


print("Select operation:")
print("a. Kilometer to Mile")
print("b. Mile to Kilometer")
option = input("Enter your choice (a or b): ")

if option == 'a':
    km = float(input("Enter the distance in kilometers: "))
    miles = km * 0.621371
    miles_rounded = round(miles, 2)
    print(str(km) + " kilometers is equal to " + str(miles_rounded) + " miles.")
elif option == 'b':
    miles = float(input("Enter the distance in miles: "))
    km = miles / 0.621371
    km_rounded = round(km, 2)
    print(str(miles) + " miles is equal to " + str(km_rounded) + " kilometers.")
else:
    print("Wrong decision")