# def to_utf8(s: str) -> bytes:
#     return s.encode('utf-8')

# text = input("შეიყვანეთ ტექსტი: ")
# utf8= to_utf8(text)
# print(utf8)

# def String(s):
#     import re
#     s = re.sub(r'\s+', ' ', s).strip() 
#     s_lower = s.lower()    
#     if 'python' in s_lower:
#         s_lower = re.sub(r'python', 'Python', s_lower)
#         return s_lower
#     else:
#         return s_lower + ' Python'

# text= input("შეიყვანეთ ტექსტი: ")
# result = String(text)
# print(result)


# def NAXEVARI(s):
#     half = len(s) // 2  
#     return s[:half]  

# string = input("შეიყვანეთ სტრიქონი: ")
# result = NAXEVARI(string)
# print("პირველი ნახევარი:", result)

# import string

# def valid(text):
    
#     allowed_chars = string.ascii_letters + string.digits

#     has_letter = any(char in string.ascii_letters for char in text)
#     has_digit = any(char in string.digits for char in text)
#     all_allowed = all(char in allowed_chars for char in text)

#     return has_letter and has_digit and all_allowed

# # გამოყენება:
# user_input = input("შეიყვანეთ სტრიქონი: ")

# if valid(user_input):
#     print("სტრიქონი ვალიდურია")
# else:
#     print("სტრიქონი არავალიდურია")  

; text = input("შეიყვანეთ სტრიქონი: ")

; text_bytes = text.encode('utf-8')
; print("სტრიქონი ბაიტებში:", text_bytes)

; decoded_text = text_bytes.decode('utf-8')
; print("ბაიტებიდან დაბრუნებული სტრიქონი:", decoded_text)
