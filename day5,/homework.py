"""day 5:
homework:

შექმენით ცვლადები 10 წიგნისთვის ( სახელი ცალკე, ფასი ცალკე, 
5 წიგნს გაუკეთეთ 10%იანი ფასდაკლება, 5 წიგნს გაუკეთეთ 20%იანი ფასდაკლება) 

იგივე წესებით, რაც გაკვეთილზე ავხსენით """


book1="chapter four"
book2="a little piece of heaven"
book3="nightmare"
book4="to end the rapture"
book5="save me"
book6="the stage"
book7="paradigm"
book8="the fight"
book9="girl i know"
book10="Dead life"

book1_price=10
book2_price=20
book3_price=30
book4_price=40
book5_price=50
book6_price=60
book7_price=70
book8_price=80
book9_price=90
book10_price=100

discount1=10
discount2=20

print(book1_price - book1_price * discount1 / 100 )
print(book2_price - book2_price * discount1 / 100 )
print(book3_price - book3_price * discount1 / 100 )
print(book4_price - book4_price * discount1 / 100 )
print(book5_price - book5_price * discount1 / 100 )

print(book6_price - book6_price * discount2 / 100 )
print(book7_price - book7_price * discount2 / 100 )
print(book8_price - book8_price * discount2 / 100 )
print(book9_price - book9_price * discount2 / 100 )
print(book10_price - book10_price * discount2 / 100 )

