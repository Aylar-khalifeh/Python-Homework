

#soal 1:

while True:
    number=int(input("enter yout number:"))

    if number % 15 ==0:
        print("Fizzbuzz")
    elif number %5==0:
        print("Buzz")
    elif number % 3 ==0:
        print("Fizz")

    else:
        print(number)


#soal 2


books={}

respons=True

while respons:
    name=input("enter your name:")
    book=input("what is your favotite book:")
    books[name]=book

    repeat=input("would you like to let another person response?")
    if repeat=='no':
        respons=False

print("...Result...")
for name , book in books.items():
    print(f"{name} loves reading {book}")




#soal 3

shopping_cars=['milk','bread','eggs','apple']
purchesed_items=[]

while shopping_cars:

    cart=shopping_cars.pop()
    purchesed_items.append(cart)

for item in purchesed_items:
  print(f"Purchasing:{item} ")

print(purchesed_items)



#soal 4


users=['admin','john','sara','mike']
user_info={}

while users:
    name =input("enter your name:  ('Exit' for exit) ")


    if name=="Exit" :
     break
    elif name in users:
     age=int(input("enter yout aga:"))
     city=input("enter your city:")


            
     user_info[name]={"name":name , "age":age , "city":city}
    

    else:
      print("user not found")


print(user_info)
