# for <variabe> in <iterable_object>:
# code to execute

# u = [1, 2, 3, 4, 5]
# for i in u:
#     print(i)



# range (start, stop, step)
#range(10) > start=0, stop=9, step=1
#range(1, 10) > start=1 stop=9 step=1
#range(1, 10, 2) > start=1 stop=9 step=2






# for i in range(1, 101):
#     print(i)

# total = 0
# for i in range(1, 101):
#     total = total + i

# print(total)


# print(sum(range(1, 100)))



# print(sum(range(3, 101, 3)))

# total = 0
# for i in range(3, 101, 3):
#     total = total+i
    
# print(total)    


# total = 0
# for i in range(3, 101 ,3):
# for i in range(5, 101, 5):
 
        
#     total = total+i

# print(total)    
    
# a = 10
# b = 20
# total = a + b 
# print("the sum of ",a, "and", b, "is", total, ".")
# e = "the sum of {} and {} is {}".format(a, b, total)
# print(e)
# abc = f"the sum of {a} and {b} is {total}."
# print(abc)  


# while loop
# while < condition>:
    # code for execution

# a =  1
# while a < 10:
#     print(f"I am inside loop for {a} times.")
#     a = a + 1    


# a = input("take username: ")
# b = input("take password: ")
# while a != "abc@gmai;.com" or b != "12345":
#     a = input("enter username:")
#     b = input("enter password: ")
#     print("success")


# a = ["utsab", "sushil", "nirajan", "ronat"]
# output = []
# for i in a :
#     output.append(i.capitalize())
#     print(output) 

# email = ["1@gmail.com", "2@gmail.com", "3@yahoo.com", "4@outlook.com", "5@gmail.com",]
# output = []
# for i in email :
#     if i.endswith("@gmail.com"):
#         output.append(i)
#         print(output)
    

# heros = ['spider man','thor','hulk','iron man', 'captain america']
# x = heros.insert( 3, 'black_panther')
# print(heros)

# heros = ['spider man','thor','hulk','black_panther', 'iron man', 'captain america']
# x = heros[1:3] = ["doctor_strange"]
# print(heros)




# heros = ['spider man','thor','hulk','black_panther', 'iron man', 'captain america']
# x = len(heros)
# print(x)



# for i in range(1, 10):
#     if i % 7 == 0:
#         break
#     print(i)

# for i in range(1, 10):
#     if i % 7 == 0:
#         continue
#     print(i)