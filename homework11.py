# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip 
# ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

# list_1=[1, 2, 3]
# list_2=['a', 'b', 'c'] 
# def group_list(*tuple):
#     return list(zip(*tuple))
# result=group_list(list_1, list_2)
# print(result)

# ////////////////////////////////////////////////

# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
#  ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  

# params:[1, 2, 3, 4, 5] 
# output: 120


# from functools import reduce

# def multiply_list_elements(params):
#     try:
#         if not params:
#             return 0
#         return reduce(lambda x, y: x * y, params)
#     except TypeError:
#         return "შეცდომა: შეიყვანეთ სია, რომელიც შეიცავს მხოლოდ რიცხვებს"

# params=[1, 2, 3, 4, 5] 
# result=multiply_list_elements(params)
# print(result)

# ///////////////////////////////////////

# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]


# odd_numbers = lambda lst: list(filter(lambda x: x % 2 != 0, lst)) if isinstance(lst, list) else "შეცდომა: პარამეტრი უნდა იყოს სია"

# params = [1, 2, 3, 4, 5, 6, 7]
# result = odd_numbers(params)
# print(result)  


# //////////////////////////////////////////////////////////////////////////////////////////


# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). 
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. 
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც 
# აღმოჩნდა ისიც გაითვალისწინეთ.

# odd_numbers = lambda lst: list(filter(lambda x: x % 2 != 0, lst)) if type(lst) == list else "შეცდომა: პარამეტრი უნდა იყოს სია"

# params = [1, 2, 3, 4, 5, 6, 7]
# result = odd_numbers(params)
# print(result)  # [1, 3, 5, 7]



# def filter_ending(strings, ending):
#     try:
#         if type(strings) != list:
#             raise TypeError("პარამეტრი strings უნდა იყოს სია")
#         if type(ending) != str:
#             raise TypeError("პარამეტრი ending უნდა იყოს სტრიქონი")

#         return list(filter(lambda s: type(s) == str and s.endswith(ending), strings))

#     except TypeError as e:
#         return f"TypeError: {e}"
#     except Exception as e:
#         return f"სხვა შეცდომა: {e}"

# params = ['hello', 'world', 'coding', 'nod']
# ending = 'ing'
# print(filter_ending(params, ending))  # ['coding']
