# Repitition Statements
# Data types allows to be iterated: Lists, Ranges, Sets.Tuple, Strings

# x = range(5,11)
petName = ["snowy", "blacky", "bruno"]

# for loop
# for(initialization;condition;incrementation/decre) - JAVA
# for num in x:
#     print(num)

# # Slicing a lists
for name in petName[3:0:-1]:
    print(name)
    
# user = {
#     "first_name" : "Johhny",
#     "last_name" : "Tadea",
#     "age" : 25,
#     "average" : 81.76,
#     "list_subjects" : ["Programming", "Mathematics", "English"]
# }

# ctrl + / - shortcut for comment
# for key in user:
#     print(key, ":", user[key])

# Looping List of Dictionaries
# list_of_users = [
#     {
#     "first_name" : "Johhny",
#     "last_name" : "Tadea",
#     "age" : 25,
#     "average" : 81.76,
#     "list_subjects" : ["Programming", "Mathematics", "English"]
#     },
#     {
#     "first_name" : "Rose",
#     "last_name" : "Tadea",
#     "age" : 23,
#     "average" : 82.54,
#     "list_subjects" : ["Programming", "Mathematics", "English"]
#     },
#     {
#     "first_name" : "Angel",
#     "last_name" : "Tadea",
#     "age" : 27,
#     "average" : 86,
#     "list_subjects" : ["Programming", "Mathematics", "English"]
#     }
# ]

# for key in list_of_users:
#     for x in key:
#         print(x, ":", key[x])