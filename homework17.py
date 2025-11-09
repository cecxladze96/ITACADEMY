# 1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y. 
# კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ ვექტორების დამატება და __str__ მეთოდი, 
# რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".

# მაგალითად:
# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)  # Output: (5, 7)

# class Vector:
#     def __init__(self, X, Y):
#         self.X=X
#         self.Y=Y
#     def __add__(self, other):
#         return Vector(self.X+other.X, self.Y+other.Y)

#     def __str__(self):
#         return f"({self.X}, {self.Y})"

# v1 = Vector(3, 5)
# v2 = Vector(2, 4)
# v3 = v1 + v2

# print(v1)  
# print(v2) 
# print(v3)    

###################################################################################

# 2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი,
#  რომელიც შეამოწმებს ორი წიგნის ტოლობას. ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

# მაგალითად:
# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  # Output: True
# print(book1 == book3)  # Output: False

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __eq__(self,other):
#         return bool(self.author==other.author and self.title == other.title)
    
# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  
# print(book1 == book3)

###################################################################################

# 3. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და
#  მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.
# Car კლასს დაუმატეთ  თითოეული ატრიბუტისთვის set და get თვისებები მათი ცვლილებებისთვის.
# დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი
#  რომ იყოს ყოველთვის მთელი და ა.შ.

# class Car:
#     def __new__(cls, *args, **kwargs):
#         print("ახალი მანქანის ობიექტის შექმნა...")
#         return super().__new__(cls)  

#     def __init__(self, brand, model, year):
#         self.brand = brand   
#         self.model = model
#         self.year = year

#     @property
#     def brand(self):
#         return self.__brand

#     @brand.setter
#     def brand(self, value):
#         if not isinstance(value, str):
#             raise ValueError("Brand must be a string")
#         self.__brand = value

#     @property
#     def model(self):
#         return self.__model
#     @model.setter 
#     def model(self, value):
#         if not isinstance(value,str):
#             raise ValueError("model must be a string")
#         self.__model= value


#     @property
#     def year(self):
#         return self.__year

#     @year.setter
#     def year(self, value):
#         if not isinstance(value, int):
#             raise ValueError("year must be a number")
#         self.__year = value

    
# car1 = Car("Mercedes", "CLA", 2024)
# print(car1.brand)  
# print(car1.model) 
# print(car1.year)   

