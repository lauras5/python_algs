# declare dictionary, python implements dictionaries as hash tables
dict = [
    {'Name': 'Larry', 'Age': 30, 'Class': 'CS270'},
    {'Name': 'Linda', 'Age': 30, 'Class': 'CS270'}
]
# dict.clear()
# del dict

# access w/ key
for x in range(len(dict)):
    print(dict[x]['Name'])

for x in dict:
    print(x['Name'])

print(dict)


