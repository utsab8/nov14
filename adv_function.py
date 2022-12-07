# def outer():
#     print("i am outer function")
#     def inner():
#         print("i am inner function")
#     inner()

# outer()    


# def welcome(name):
#     print(f"welcome {name}!")
    
# a = welcome
# a("utsab")


# def increment(num):
#     def increase_by(factor):
#         return num + factor
#     return increase_by
# increase_by = increment(20)
# print(increase_by(30))
# print(increase_by(50))

# def increment(num):
#     def increase_by(factor):
#         return num + factor
#     return increase_by

# increase_by = increment(50)
# print(increase_by(20))
# print(increase_by(50))

# def welcome(name):
#     print(f"welcome{name}")

# def greet_ram(a):
#     a("utsab")
    
# greet_ram(welcome)


# higher order funcation
# decorator

# def welcome(name):
#     print(f"welcome{name}")

# def bye_bye(name):
#     print(f"bye_bye{name}") 

# def greet_ram(a):
#     a("ram")

# greet_ram(bye_bye)
# greet_ram(welcome)


# def decorate_funcaion(func):
#     def wrapper():
#         print("called before.")
#         func()
#         print("called after")
#     return wrapper

# @decorate_funcaion
# def example():
#     print("i am utsab")
# example()


def smart_decorate(func):
    def wrapper(a, b):
        if b== 0:
            return "can not divide by zero."
        else:
            return func(a, b)
    return wrapper

@smart_decorate
def division(a, b):
    return a / b

print(division(10,2))
print(division(10,0))
