# n=int(input("დაწერეთ რიცხვი:" ))

# num_sum=0
# for i in range(1, n+1):
#  num_sum += i
# print("1-დან", n , "-მდე რიცხვის ჯამი არის", num_sum)


# n=int(input("დაწერეთ რიცხვი:" ))
# while n>0:
#     print(n, end=", " if n > 1 else "\n")
#     n-=1
# 

# import random
# secret_numb = random.randint(1, 100)
# while True:
#       guess=int(input("ჩაიფიქრე რიცხვი 1-იდან 100=მდე:" ))
#       if guess == secret_numb:
#             print("გილოცავთ, სწორად გამოიცანით")
#             break
#       elif guess < secret_numb:
#         print("ძალიან პატარა რიცხვია")
#       else: print("ძალიან დიდი რიცხვია")


# total_sum = 0

# while True:
#     num_input = input("ჩააწერეთ რიცხვი ან 'sum' შეწყვეტისთვის: ")
    
#     if num_input == 'sum':
#         break
    
#     try:
#         number = float(num_input)
#         if number > 0:
#             total_sum += number
#     except ValueError:
#         print("გთხოვთ შეიყვანოთ რიცხვი ან 'sum'.")
        
# print("დადებითი რიცხვების ჯამი:", total_sum)


