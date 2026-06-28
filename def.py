#soal 1

def car_info(brand,model,year=' '):

    y=f"{brand} {model}"
    if year:
        y=f"{brand} {model} {year}"

    return y

car=car_info("pegu","206",)
print(car)



#soal 2

def Book(title,author):

    book_info=f"{title} from {author}"
    return book_info


y=Book("python","Eric Matthes")
print(y)


#soal 3

def username(frist_name,last_name):
    ful_name=f"{frist_name} {last_name}"
    return ful_name


while True:
    print("Enter 'q' for exit ")
    f_name=input("Enter your frist name:")
  

    l_name=input("Enter your last name:")
    if l_name and f_name=='q':
        break


    nam=username(f_name,l_name)
    print(f"welcome{nam}")

#soal 4

def pet_info(name_animal,tyle_animal='cat'):

    print(f"{name_animal} is a {tyle_animal}")


pet_info('gigi')



#soal 5

def make_pizza(orders,completed_orders):
    
    while orders:
        current_order=orders.pop()
        print(f"perpering pizza {current_order}")
        completed_orders.append(current_order)
    

def show_pizza(completed_orders):
    for order in completed_orders:
        print(order)


orders=['pizaa','burger','pasta']
completed_orders=[]

make_pizza(orders,completed_orders)
show_pizza(completed_orders)


#soal 6

def student(frist_name,last_name,**stu_info):
    stu_info['frist name']=frist_name
    stu_info['last name']=last_name
    return stu_info


user_profile=student('Ali','Ahmadi',university='Sharif',major='Computer',age= 22)
print(user_profile)


#soal 7

def registration_stu(frist_name,last_name,major,age):
    person={'frist name':frist_name,'last name':last_name,'major':major,'age':age}
    return person

students=[]
while True:
    f_name=input("Enter your name:")
    if f_name=='q':
        break
    l_name=input("Enter your last name:")
    major_1=input("Enetr your major:")
    age_1=input("Enetr your age:")



    stu=registration_stu(f_name,l_name,major_1,age_1)
    students.append(stu)
    print(students)

