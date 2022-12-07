

# TAKE NAME , CLASS, ROLL NUMBER AS INPUT
fname = input("take your name: ")
ec = input("input your class: ")
rl = input("Enter your roll number: ")
print(fname)
print(ec)
print(rl)

a = input("micro_processor marks : ")
b = input("visual_programming  marks : ")
c = input("digital_logic marks: ")
total = int(a)+int(b)+int(c)
print(total)
percentage = (total/300)*100
print(percentage)
if percentage < 40:
    print("fail")
else:
    print("pass")

    
            








