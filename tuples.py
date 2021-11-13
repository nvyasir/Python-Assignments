# Tuples
#
# You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the contact.
# Complete the program to get a string as input, search for the name in the list of contacts and output the age of the contact in the format presented below:
#
# Sample Input
# John
#
# Sample Output
# John is 31

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()

index_num = 0
length = len(contacts)

for i in contacts:
    if name not in i:
        index_num+=1
    if name in i:
        print(name + " is "+ str(contacts[index_num][1]))
        break
    if index_num >= length:
        print("Not Found")


