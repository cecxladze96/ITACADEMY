# elements = input("შეიყვანეთ რიცხვები (გამოყავით დაშორებით): ")
# numbers = set(map(int, elements.split()))
# print("უნიკალური რიცხვები:", numbers)

############################

# elements = input("შეიყვანეთ რიცხვები (გამოყავით დაშორებით): ")
# numbers = frozenset(map(int, elements.split()))
# print("შეუცვლელი უნიკალური რიცხვები:", numbers)

############################

# arr1={12,13,14,17,19}
# arr2={18,11,21,17,22}

# arr3=arr1.union(arr2)
# result=tuple(arr3)
# print(result)

############################

# elements =input("შეიყვანეთ რიცხვები (გამოყავით დაშორებით): ")
# numbers = list(map(int, elements.split()))
# tuple_elements=tuple(numbers)
# numbers_list = list(set(tuple_elements))
# print("უნიკალური ელემენტები სია:", numbers_list )

############################

# people=[("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# for name, age in people:
#     print(f"Name: {name}, Age: {age}")


############################


# names1=["Irakli", "Giorgi", "Nona", "Oto"]
# names2=["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

# set_names1=set(names1)
# set_names2=set(names2)

# same_names=set_names1.intersection(set_names2)
# print(same_names)