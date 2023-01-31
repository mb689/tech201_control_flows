# Looping

# A for loop is where you define an iterator number and cycle through data (lists) 'foreach' entry in that data structure #

# Creating a for loop

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}

for num in list_data:
    print(num * 2)

for data in embedded_lists:
    print(data)

for data in embedded_lists:
    for num in data:
        print(num)


# Loops for dictionaries

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)