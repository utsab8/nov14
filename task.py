student_score = [
    {"name": "Ram", "score": 80},
    {"name": "Sita", "score": 100},
    {"name": "Abc", "score": 30},
    {"name": "xyz", "score": 40},
    {"name": "john", "score": 37},
    {"name": "shyam", "score": 90},
    {"name": "hari", "score": 36},
]

for i in student_score:
    print(i)
















colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
# take user input teo times which color to be removed.
#and remove those colors


colors_chosen = []

while colors :
#     print("please select a color from this list:{}".format(colors))
    color_selected = input("Select the first remove color in this list:{}".format(colors))

    # while color_selected not in colors:
    #     print("the color selected is not one of the option")
        # print("Select the second remove color in this list: {}".format(colors))
        # color_selected = input("Select the second remove color in this list: {}".format(colors))

    colors.remove(color_selected)
    colors_chosen.append(color_selected)

# print("these are the color you chose: {}".format(colors_chosen))