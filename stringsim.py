# Reading a file
# Source :

# s = ""

# with open('./uploads', 'r') as file:
#     s = s + file.read().replace("\n", " ")

# file.close()

# print (s)


import os

entries = os.listdir('./uploads')

s = ""

for i in entries :
    
    with open(f'./uploads/{i}', 'r') as file:
        s = s + file.read().replace("\n", " ")


print(s)

# print(type(s))

