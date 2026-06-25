

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