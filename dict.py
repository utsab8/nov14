# a = {} > empty dictionary
# a = {"name": "ram","address": "pyuthan", "contact": "9866601808"}
# x = a.get('collage','abc collage')
# print(x)




# a = {"name": "ram","address": "pyuthan", "contact": "9866601808"}
# x = a.setdefault("phone", "986660101")
# print(x)
# print(a)


#pop pop-item
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.popitem()
# print(car)


# a ={}
# b = ["name", "address", "contact", "following"]
# x = a.fromkeys(b, "utsab")
# print(x)

# c= {'name': 'None', 'address': 'None', 'contact': 'None', 'following': 'None'}
# a = c['name'] = "utsab"
# b = c['address'] = "pyuthan"
# d = c['contact'] = 9866601808
# e = c['following'] = 0
# f = c['education'] = "diploma"
# print(a,b,d,e,f)

# c = {'name': 'None', 'address': 'None', 'contact': 'None', 'following': 'None'}
# a = c.pop("contact")
# print(a)

# c = {'name': 'None', 'address': 'None', 'contact': 'None', 'following': 'None'}
# for i in c.values():
#     print(i)

# c = {'name': 'Utsab', 'address': 'Pyuthan', 'contact': 9866601808, 'following': '16'}
# for i in c :
#     print(i)


# items()

# # a, b, c = 10, 20, 30
c = {'name': 'Utsab', 'address': 'Pyuthan', 'contact': 9866601808, 'following': '16'}
x = c.items()
for a , b in c.items():
    print(a , b)