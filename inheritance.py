# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#     def profile(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")

# class Student(Person):
#     def __init__(self, name, address, roll_no):
#         super().__init__(name, address)
#         self.roll_no = roll_no

#     def profile(self):
#         super().profile()
#         print(f"Roll number {self.roll_no}")

# class Teacher(Person):
#     def __init__(self, name, address, designation):
#         super().__init__(name, address)
#         self.desihnation = designation

# s = Student("Ram", "kathmandu", 12)
# s.profile()


# class User:
#     def __init__(self, _id, username, pwd):
#         self._id = _id
#         self.username = username
#         self.password = pwd
        

# class Person(User):
#     def __init__(self, _id, username, pwd, name, address):
#         super().__init__(_id, username, pwd)
#         self.name = name
# #         self.address = address

#     def profile(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")


# class Staff(Person):
#     def __init__(self, _id, username, pwd, name, address, designation):
#         super().__init__(_id, username, pwd, name, address)
#         self.designation = designation

#     def Profile(self):
#         super().profile()
#         print(f"id :{self._id}")
#         print(f"username: {self.username}")
#         super().profile()
#         print(f"designation: {self.designation}")
        

# s = Staff(1, "ut@.com", "1234", "utsab", "pyuthan", "admin")
# s.profile()



# student_score = [
#     {"name": "Ram", "score": 80},
#     {"name": "Sita", "score": 100},
#     {"name": "Abc", "score": 30},
#     {"name": "xyz", "score": 40},
#     {"name": "john", "score": 37},
#     {"name": "shyam", "score": 90},
#     {"name": "hari", "score": 36},
# ]
# out = []
# for i in student_score:
#     score= i.get("score")
#     if score >= 40:
#         out.append(i)
# print(out)

# output = list(filter(lambda i:i.get("score") >= 40, student_score))
# print(output)


# colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
# remove = ["yellow", "red"]
#remove these color from remove list










# colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
# # take user input teo times which color to be removed.
# #and remove those colors


# colors_chosen = []

# while colors :

#     color_selected = input("Select the  remove color from in this list:{}".format(colors))


#     while color_selected not in colors:
#         print("the color selected is not one of the option")
       
#         color_selected = input("Select the  remove color in this list: {}".format(colors))
        

#     colors.remove(color_selected)
#     colors_chosen.append(color_selected)

# print("these are the color you chose: {}".format(colors_chosen))




# colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
# remove = ["yellow", "red"]
# def remove_common(a, b):
#     for i in a[:]:
#         if i in b:
#             a.remove(i)
#             b.remove(i)

#     print("colors :", a)
#     print("remove:", b)

# if __name__ == "__main__":
#     remove_common(colors, remove)