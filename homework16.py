# 1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. ასევე, შექმენით კლასის მეთოდი car_info(),
#  რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

# class car:
#     def __init__(self,Brand, Model, Year):
#         self.Brand=Brand
#         self.Model=Model
#         self.Year=Year

#     def car_info(self):
#       print(f"ბრენდი: {self.Brand}")
#       print(f"მოდელი: {self.Model}")
#       print(f"წელი: {self.Year}")

# my_car=car("Mercedes", "CLA", 2024)    
# my_car.car_info()



###################################################################

# 2. Car კლასში დაამატეთ მეთოდი age_of_car,
# რომელიც დაითვლის მანქანის ასაკს. ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.

# import datetime

# class car:
#     def __init__(self,Brand, Model, Year):
#         self.Brand=Brand
#         self.Model=Model
#         self.Year=Year
#     def Age_of_car(self):
#        current_year=datetime.datetime.now().year
#        return current_year-self.Year
    

#     def car_info(self):
#       print(f"ბრენდი: {self.Brand}")
#       print(f"მოდელი: {self.Model}")
#       print(f"წელი: {self.Year}")
#       print(f"მანქანის ასაკი: {self.Age_of_car()} წელი")

# my_car=car("Mercedes", "CLA", 2024 )    
# my_car.car_info()


###################################################################

# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს. 
# დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(),
# რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".

# class car:
#     def __init__(self,Brand, Model, Year):
#         self.Brand=Brand
#         self.Model=Model
#         self.Year=Year

#     def car_info(self):
#       print(f"ბრენდი: {self.Brand}")
#       print(f"მოდელი: {self.Model}")
#       print(f"წელი: {self.Year}")

# class ElectricCar(car):
#     def __init__(self,Brand,Model,Year, Battery_life):
#         super().__init__(Brand, Model, Year)  
#         self.Battery_life = Battery_life 
#     def battery_info(self):
#         print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.Battery_life} საათი")


# my_tesla = ElectricCar("Tesla", "Model M", 2024, 16)
# my_tesla.car_info()
# my_tesla.battery_info()

###################################################################

# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. 
# გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას.

# class car:
#     Car_number=0
#     def __init__(self,Brand, Model, Year):
#         self.Brand=Brand
#         self.Model=Model
#         self.Year=Year
#         car.Car_number+=1  

#     def car_info(self):
#       print(f"ბრენდი: {self.Brand}")
#       print(f"მოდელი: {self.Model}")
#       print(f"წელი: {self.Year}")

# car1 = car ("Mercedes", "CLA", 2024)    
# car2 = car("BMW", "X5", 2020)
# car3 = car("Toyota", "Camry", 2021)
# car4 = car("Mercedes", "CLA", 2024)

# car1.car_info()
# car2.car_info()
# car3.car_info()
# car4.car_info()

# print(f"\nსულ შექმნილია {car.Car_number} მანქანა.")


###################################################################

# 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.
# class car:
#     Car_number=0
#     def __init__(self,Brand, Model, Year):
#         self.Brand=Brand
#         self.Model=Model
#         self.Year=Year
#         car.Car_number+=1  

#     def car_info(self):
#       print(f"ბრენდი: {self.Brand}")
#       print(f"მოდელი: {self.Model}")
#       print(f"წელი: {self.Year}")

#     @classmethod
#     def total_cars(cls):
#         print(f"სულ შექმნილია {cls.Car_number} მანქანა.")

# car1 = car ("Mercedes", "CLA", 2024)    
# car2 = car("BMW", "X5", 2020)
# car3 = car("Toyota", "Camry", 2021)
# car4 = car("Mercedes", "CLA", 2024)

# car1.car_info()
# car2.car_info()
# car3.car_info()
# car4.car_info()        
# car.total_cars()    