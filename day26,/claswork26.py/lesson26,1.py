def print_name(name,amount = 5):
    for i in range(amount):
        print(name)

print_name("luka",10)


def print_name(name,amount = 5):
    names = []
#ამ შმთხვევაში ჩვენ შგვიძლია names სიაში შვიტანოთ 
#ჩვენი name მნიშვნილობა თავისივე რაოდენობით.
    for i in range(amount):
        names.append(name)

print_name("luka",10)


#ეხლა ვთქვათ რომ ჩენ გვინდა names სია გამოვიყენოთ ფუნქციის გარეთ.
#ამ შემთხვევაში names სია არის ლოკალური ცვლადი.
#ლოკალური ცვლადი ქვია ისეთ ცვლადს რომელიც ფუნქციის გარეთ ხელმისაწვდომი არარის აქედან გამომდინარე
#ჩვენ არ შეგვიძლია ფუნქციის გარეთ names ცვლადის გამოძახება.
def print_name(name,amount = 5):
    names = []
    for i in range(amount):
        names.append(name)
#print(names)

#ეს უკვე ერორია
#მაშინ ჩვენ შემოვიტანთ return ფუნქციას.

def create_list(name,amount = 5):
    names = []
    
    for i in range(amount):
        names.append(name)

        return names  
#ახლა შევქმნით ცვლადს და მასში შევიტანთ create_list("luka")ამ მნიშვნელობას და გამოვიძახებთ print ფუნქციით.
result = create_list("luka") 
print(result)





