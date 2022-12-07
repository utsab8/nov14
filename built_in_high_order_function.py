#lambda

# total = lambda a, b:a+b
# print(total(10, 5))

# map
# def increment_by_one(n):
#     return n+1
# a = [1, 2, 3, 4, 5, 6, 7, 8,]
# out = map(lambda n:n+1, a)
# print(list(out))

# names = ["utsab", "shyam", "sita", "hari", "gita"]
# x = map(lambda names:names.capitalize(), names)
# print(list(x))


#filter
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def is_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
#     return num % 2 == 0
# out = filter(lambda num:num % 2 == 0, a)
# print(list(out))

# emails = ["1@gmail.com", "2@gmail.com", "3@gmail.com", "4@outlook.com"]
# x = filter(lambda emails: emails.endswith(@gmail.com), emails)
# print(list(emails))

# d = [17, 20, 25, 30]
# print(sum(d))

# c = ["17", "20", "25", "30"]
# total = 0
# for i in c :
#         total = total +int(i)


# c = ["17", "20", "25", "30"]
# print(sum(map(int, c)))


a = "457d89e36"
total = 0
for i in a:
    if i.isnumeric():
        total = total + int(i)

print(total)