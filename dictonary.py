#we have the following dictionary containing details:

# useer ={
#     "user name" :"my_user",
#     "password": "test@123",
#     "email": "my_email@example.com",
#     "address": "ABC road, 11111",
#     "countery": "India"
# }

"""
Delete the sencetive information from the dictonary prsent in a list
sensetive_Info = ["password", "address"]

"""

user ={
    "user name" :"my_user",
    "password": "test@123",
    "email": "my_email@example.com",
    "address": "ABC road, 11111",
    "countery": "India"
}
sensetive_info = ["password", "address"]

# for key in user:
#     if key in sensetive_info:
#         user.pop(key)
#
# print(user)
for i in sensetive_info:
    print(f"key: {i}, value: {user[i]}")
    user.pop(i)
print(user)
