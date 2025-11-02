# def fibonacci(n):
#     fibonacci_list = []
#     a, b = 0, 1
#     for i in range(n):
#         fibonacci_list.append(a)
#         a, b = b, a + b
#     return fibonacci_list

# n = int(input("შეიყვანეთ ფიბონაჩის n-ელემენტი: "))
# print(fibonacci(n))

#################
# def anagrams(str1,str2):
#     sorted_str1=sorted(str1)
#     sorted_str2=sorted(str2)
#     return sorted_str1==sorted_str2

# str1=input("შეიყვანეთ პირველი სიტყვა:")
# str2=input("შეიყვანეთ მეორე სიტყვა:")

# if anagrams(str1, str2):
#     print("სტრიქონები არის ანაგრამები.")
# else:
#     print("სტრიქონები არ არის ანაგრამები.")

#################

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# num=int(input("შეიყვანეთ რიცვი :"))
# print(f"{num}-ის ფაქტორიალი არის: {factorial(num)}")


#################

# def func(string,char):
#     count = 0
#     for i in string:
#         if i == char:
#             count += 1
#     return count
# text = input("შეიყვანეთ სტრიქონი: ")
# symbol = input("შეიყვანეთ სიმბოლო: ")

# print(f"სიმბოლო '{symbol}' სტრიქონში მეორდება {func(text, symbol)} ჯერ.")
        