# While Loops

# While loops monitor data rather than iterate

x = 0

# while x < 10:
#     print(f"it's working -> {x}")
#     x += 1

# Using break

# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break
#     x += 1


# verify someone's age
# This can either be an int (20) or string twenty

# age = input("What is you age? ")
#
# print(f"Your age is {age}")

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit():
        print(f"Your age is {age}")
        user_prompt = False
    else:
        print(f"{age}, not a valid number")