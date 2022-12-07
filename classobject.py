# 1. class and object
# 2. Inheritance
# 3. Abstraction
# 4. polymorphism


# class Student:
#     def __init__(self, _id, roll_no, name, gender):
#         self._id = _id
#         self.roll_number = roll_no
#         self.name = name
#         self.gender = gender 
#         self.total_attendence = 0
#     def view_attendence(self):
#         return f"Total attendence of {self.name} is {self.total_attendence}" 

# s = Student(1, 2, "utsab", "mail")
# print(f"Name: {s.name}")
# print(f"roll number: {s.roll_number}")
# print(s.view_attendence())
# s2 = Student(2, 3, "sita", "female")
# print(s2.view_attendence())


# students = []
# for i in range(1, 6):
#     roll_no = input("enter roll number: ")
#     name = input("enter the name: ")
#     gender = input("enter the gender: ")
#     s = Student(i, roll_no, name, gender)
#     students.append(s)

# for student in students:
#     print(f"name: {student.name}")
#     print(f"Roll number: {student.roll_number}")
#     print(student.view_attendence())
#     print("-"*50)



    #staff =>id name post contact
# class Staff:
#     def __inti__(self, _id, name, post, contact, gender):
#         self._id = _id
#         self.name = name
#         self.post = post
#         self.contact = contact
#         self.gender = gender
#         self.total_attendence = 0
#     def view_attendence(self):
#         return f"Total attendence of {self.name} is {self.total_attendence}"
    
# student = []
# for i in range(1, 3):
#     id = input("enter the id number: ")
#     name = input("enter the name : ")
#     post = input("enter the post: ")
#     contact = input("enter the contact no: ")
#     gender = input("enter the gender: ")

#     s = Staff()
#     student.append(s)


# for students in student:
    
#     print(f"name: {student.name}")
#     print(f"id: {student.id}")
#     print(f"post:{student.post}")
#     print(f"contact :{student.contact}")
#     print("gender: {student.gender}")
#     print(student.view_attendence())
#     print("-"*50)








# class Staff:
#     def __init__(self, _id, roll_no, name, gender):
#         self._id = _id
#         self.contact = contact
#         self.name = name
#         self.post = post
        
#         self.total_attendence = 0
#     def view_attendence(self):
#         return f"Total attendence of {self.name} is {self.total_attendence}" 




# staffs = []
# for i in range(1, 6):
#     id = input("enter id number: ")
#     name = input("enter the name: ")
#     post = input("enter the post: ")
#     contact = input("enter the contact no: ")
#     gender = input("enter the gender: ")
    
#     s = Staff(i, id, name, post)
#     staffs.append(s)

# for a in staffs:
#     print(f"name: {a.name}")
#     print(f"id: {a._id}")
#     print(a.view_attendence())
#     print("-"*50)



# <----------------------------------------------------------------------------------------------------------------------------------------->


# class Product:
#     def __init__(self, name, sku, price):
#         self.name = name
#         self.sku = sku
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price <=0 :
#             raise ProductpriceError("price can not be smaller than zero")
            
#         self.__price = price
        
# tshirt = Product("T-shirt", "123", 500)
# print(tshirt.__dict__)
# try:
#     tshirt.price = -200
#     except ProductpriceError as err
# # print(f"price of T-shirt: {tshirt.price}")
# print(tshirt.__dict__)
# tshirt.price = -1
# print(tshirt.__dict__)




        


class Calculator:
    def __init__(self, num1, num2):
        self.num1 =num1
        self.num2 = num2
    def add(self):
        return self.num1+self.num2

    def difference(self):
        return self.num1-self.num2

    def product(self):
        return self.num1*self.num2


    @staticmethod
    def sqrt(num):
        return num**0.5

c =  Calculator(20,10)
print(c.add())
print(c.difference())
print(c.product())
print(Calculator.sqrt(25))


                  