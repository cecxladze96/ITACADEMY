
# numbers = []

# while True:
#     command = input("შეიყვანეთ სიმბოლო ('a'-დამატება, 'r'-წაშლა, 'e'-გასვლა): ")
    
#     if command == 'a':
#         try:
#             num = int(input("შეიყვანეთ სიაში დასამატებელი რიცხვი: "))
#             numbers.append(num)
#             print("განახლებული სია:", numbers)
#         except:
#             print("გთხოვთ, შეიყვანოთ რიცხვი.")
    
#     elif command == 'r':
#         if numbers:
#             try:
#                 num = int(input("შეიყვანეთ სიაშუ წასაშლელი რიცხვი: "))
#                 numbers.remove(num)
#                 print("განახლებული სია:", numbers)
#             except:
#                 print("ეს რიცხვი სიაში არ მოიძებნა.")
#         else:
#             print("სია ცარიელია")
    
#     elif command == 'e':
#         print("პროგრამა დასრულდა. საბოლოო სია:", numbers)
#         break
    
#     else:
#         print("გამოიყენეთ მხოლოდ 'a', 'r' ან 'e'.")


my_list= [43, '22', 12, 66, 210, ["hi"]]

# print("სია:", my_list)

# index=my_list.index(210)
# print(index)

# append=my_list.append("hello")
# print(my_list)

# pop=my_list.pop(2)
# print(my_list)

# my_llist_2=my_list[:]
# my_llist_2.clear()
# print(my_list, my_llist_2)



# import re

# def check_number(phone):
#     pattern = r"\(\d{3}\) \d{3}-\d{3}"
#     if re.fullmatch(pattern, phone):
#         return phone
#     else:
#         return "Invalid format"


# user_input = input("შეიყვანეთ ტელეფონის ნომერი: ")

# result = check_number(user_input)
# print(result)
