"""დუბლიკატების სია: დაწერეთ ალგორითმი, რომელიც მიიღებს სიას.
 თქვენ შემდეგ ამ სიის დუბლიკატებს გადაიტანთ ახალ სიაში და დაბეჭდავთ მას.
"""
my_list = [1, 1, 2, 3, 4, 4, 5]
duplicates = []
for i in my_list:
    if my_list.count(i) > 1:
        duplicates.append(i)

print(duplicates)