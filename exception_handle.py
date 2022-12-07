# exception handling

# try:
#     #code
#     except Exception
#     #code
#     except Exception
#     #code
#     else:
#         #code
# finally:
    #code

# try:
#     a = int(input("enter the number: "))
#     b = int(input("enter the number"))


#     print(a+b)
# except ValueError:
#     print("can not convert to integer")
# except NameError:
#     print("something is not defined")
# finally:
#     print("code is executed")
# name = input("enter the name: ")
# print(name)


# a = {"properties":{
#     "profile":{
#         "name": "ram",
#         "education":[
#             {"collage": "abc", "year":2018},
#         {"collage": "abc", "year":2018},
#         ]
#     },
#     "followers": 10000,
#     "following": 100,
#     }
# }
# name = a.get("properties").get("profile").get("name")
# following = a.get("properties").get("follwing")
# followers = a.get("properties").get("followers")
# print(f"name:{following}")
# print(f"following:{followers}")
# print(f"followers:{name.capitalize()}")
# education = a.get("properties").get("profile").get("education")
# for education in education:
#     collage = education.get("collage")
#     year = education.get("year")
#     print(f"education({year}): {collage.upper()}")

oil_price = [
    {
        "oil_type": "petrol",
        "price":[
            {"year": 2018, "price":100},
            {"year": 2019, "price":150},
            {"year": 2020, "price":200},

        ]
    },
    {
        "oil_type": "diesel",
        "prices":[
            {"year": 2018, "price":80},
            {"year": 2018, "price":100},
            {"year": 2018, "price":160},
        ]
    }
]


# average_list = []
# print("-----------------------------------------------")
# for  in oil_price:
#     gas_item = items.get("oil_type")
    
#     price_info = items.get("prices")


#     for prices in price_info:
#         year = prices.get("year")
#         prices = prices.get("price")
#         print(f"price({year}): Rs.{price}")
#         average_list.append("price")

#         total = int(sum(average_list))




print("-"*50)
for oil in oil_price:
    print(f"oil type: {oil.get('oil_type').capitalize()}")
    prices = oil.get("price")
    total_price = 0
    for price in prices:

        year = price.get('year')
        p = price.get('price')
        total_price = total_price + p
        print(f"price({year}): Rs.{p}")
    avg_price = round((total_price / len(price)), 2)
    print(f"Average price:{avg_price}")
    print("-"*50)




# print(f"oil type:{'petrol'}")
# for oil





# --------------------------------------------
# oil type: petrol
# price(2018):
# price(2018):
# price(2020):
# average price(2018-2020):
# ------------------------------------------------
# oil type: diesel
# price(2018):
# price(2018):
# price(2020):
# average price(2018-2020):