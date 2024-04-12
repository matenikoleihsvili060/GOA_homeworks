"""3) შექმენით 2 ცვლადი სადაც შეტანილი გექნებათ ადამიანის წონა და სიმაღლე, (required_weight,required_height)
რომლის მნიშვნელობაც იქნება 50 და 170 , 
შემდეგ მომხმარებელს შემოატანინეთ მისი წონა input ფუნქციის მეშვეობით
და შეამოწმეთ მომხმარებლის წონა თუ უდრის required_weight ცვლადს და მომხარებლის 
სიმაღლე თუ უდრის required_height, აგრეთვე მეორე პრინტში შეამოწმეთ თუ აღემატება წონას და ნაკლებია სიმაღლეზე,
თითქმის ყველა კომბინაცია შედარების ოპერატორების."""



required_weightm = 50
required_height = 170

weightm = int(input(" how much weight are you "))
height = int(input(" what is the height?"))
 
print(weightm == required_weightm and height == required_height)
print(weightm == required_weightm or height == required_height)
print(weightm == required_weightm and height == required_height)
print(weightm >= required_weightm and height >= required_height)
print(weightm >= required_weightm or height >= required_height)
print(weightm <= required_weightm and height <= required_height)
print(weightm <= required_weightm or height <= required_height)
