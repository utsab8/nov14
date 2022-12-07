# def hello():
#     print("hello guys")
    

# def sum_of_two_numbers(num1, num2):
#     total = num1 + num2
#     return total
# total_sum = sum_of_two_numbers(10, 15)
# print(total_sum)

# def prodect_of_two_numbers(pro1, pro2):
#     total= pro1 + pro2
#     return total
# total_number = prodect_of_two_numbers(50, 70)
# print(total_number)    


#   name = "ram"
#   name.capitalize()


# u = "utsab"
# x = u.capitalize()
# print(x)
  

# name = "Utsab"
# hello = name.casefold()
# print(hello)
 
 



# u = "u t s a b a c h a r y a"
# x = u.count("a")
# print(x)

# u = "---utsab---"
# x = u.strip("---")
# print(x)


# u = "utsab-sushil-ronat-nirajan"
# x = u.split("-", 2)
# print(x)

# u = "utsab-acharya-sushil"
# x = u.partition("-")
# print(x)

# u = "utsabacharya12@gmail.com"
# x = u.startswith("utsabacharya")
# print(x)


# u = "utsabacahrya12@gmail.com"
# x = u.endswith(".com")
# print(x)


# u = "banana"
# x = u.count("ba")
# print(x)

# u = "utsab acharya"
# x = u.find("y")
# print(x)


# u = "utsab_acharya"
# x = u.find("a",5)
# print(x)

# u = ("utsab", "sushil", "nirajan")
# x = "-".join(u)
# print(x)



# define list

# u = "utsab"
# x = u.center(50)
# print(x)


# list: collection of data
# array: collection of similar data

#dir(list)

# student = ["ram", "shyam", "utsab", "sushil"]
# student.append("nirajan")
# print(student)

# student = ["ram", "shyam", "utsab", "sushil"]
# student.clear()
# print(student)

# u = [1, 2, 3, 4, 5, 6]
# x = u.copy()
# print(x)

# student = ["u", "t", "s", "a", "b", "a", "t", "t"]
# x = student.count("t")
# print(x)


# student = ["utsab", "sushil"]
# friend = ["nirajan", "ronat"]
# student.extend(friend)
# print(student)

# student = ["utsab", "sushil", "ronat", "nirajan", "utsab"]
# x = student.index("nirajan", 1)
# print(x)

# student = ["sushil" , "ronat", "nirajan"]
# x = student.insert(2, "utsab")
# print(student)

# student = ["utsab", "sushil", "ronat" ,"nirajan"]
# x = student.pop(2)
# print(student)


# student = ["utsab", "sushil", "ronat" ,"nirajan"]
# x = student.remove("sushil")
# print(student)

# student = ["utsab", "sushil", "nirajan"]
# x = student.reverse()
# print(student)

# student = ["utsab", "sushil", "nirajan", "om", "ronat"]
# x = student.sort()
# print(student)


# student = [1, 5, 45 , 25, 85]
# x = student.sort(reverse=True)
# print(student)








#----------------------------------------------------------------#

#function

# def profile(name, address, contact):
# print(f"name:{name}")
# print(f"name:{address}")
# print(f"name:{contact}")
    
# profile("ram", "ktm", "9866601808")
# print("____________________________________")
# profile("ram", "9866601808", "ktm")

# print("____________________________________")
# profile(name="ram", address="ktm", contact="9866601808")
# print("____________________________________")
# profile(name="ram", contact="9866601808", address="ktm",)

# 

# def total_sum(num1, num2):
#         total = num1 + num2
#         print(f"total: {total}") 
# def total_sum_two(num1, num2):
#     total = num1 +num2
#     return total

# b = total_sum(10, 15)
# print(f"b: {b}")
# a = total_sum_two(10, 25)
# print(f"a: {b}")


# *args, **kwargs

# def example(*args):
#     print(args)
# example(1, 2, 3, 4, 5) 
    


# def example(**kwargs):

#     print(kwargs)

# example(name="utsab", contact="786458", nickname="ut")

# def utsab(*args, **kwargs):

#     print(args[2])
#     print(kwargs.get("name"))


# utsab( 1,2,3, name ="utsab", contact="9866601808", nickname="utsa")
    

# def multiple_of_num(num1, factor=5):
#     return num1 * factor
# print(multiple_of_num(20,))    



# def multiple_of_num(num1, factor=5):
#     return num1 * factor
# print(multiple_of_num(20, 2))    