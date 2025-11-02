# შექმენით csv  ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:


# import os, csv
# path="files"
# file_name="students.csv"
# os.makedirs(path, exist_ok=True)
# file_name=os.path.join(path, file_name)
# print(file_name)


# header = ["id", "name", "age", "grade", "subject_name", "mark"]
# data = []

# with open(file_name, "w", newline='', encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(header)  
#     writer.writerows(data)  

# print(f"CSV ფაილი '{file_name}' წარმატებით შეიქმნა.")


####################################################################################################
# 1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი შეიყვანს ინფორმაციას(id,name,age,grade,subject_name,mark) 
# და თქვენ სტუდენტს დაამატებს csv ფაილში. დაასორტირეთ მონაცემები id-ის მიხედვით.

# import os, csv
# path="files"
# file_name="students.csv"
# os.makedirs(path, exist_ok=True)
# file_name=os.path.join(path, file_name)
# print(file_name)
# new_students=[] 

# try:
#             print("\nახალი სტუდენტის მონაცემების შეყვანა:")
#             student_id = int(input("ID: "))
#             name = input("სახელი: ")
#             age = int(input("ასაკი: "))
#             grade = input("კლასი/გრადე: ")
#             subject_name = input("საგანი: ")
#             mark = float(input("შეფასება: "))
# except ValueError:
#         print("გთხოვთ შეიყვანოთ ვალიდური მონაცემები!")
# else:
#   new_students.append({
#         "id": student_id,
#         "name": name,
#         "age": age,
#         "grade": grade,
#         "subject_name": subject_name,
#         "mark": mark
#     })
  
# print("\nNew students list:", new_students)



# with open(file_name, 'a', encoding='utf-8', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=['id','name','age','grade','subject_name','mark'])
#     writer.writerows(new_students)

# new_students.sort(key=lambda x: x['id'])

# print(f"სტუდენტი წარმატებით დაემატა")


####################################################################################################
# 2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, 
# როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.


# import os, csv
# path="files"
# file_name="students.csv"
# os.makedirs(path, exist_ok=True)
# file_name=os.path.join(path, file_name)
# print(file_name)
# w1 = 10
# w2 = 20
# w3=10
# w4=10
# w5=10
# w6=10
# lines = 60
# counter = 0

# choice = input("ყველა სტუდენტი თუ კონკრეტული? (all/id): ").strip().lower()
# if choice == "all":
#     with open(file_name, "r", newline='', encoding="utf-8") as csvfile:
#         reader = csv.DictReader(csvfile) 
#         for row in reader:
#              if counter == 0:
#               head=tuple(row.keys())
#               print(f' {head[0]:{w1}}{head[1]:<{w2}}{head[2]:<{w3}}{head[3]:<{w4}}{head[4]:<{w5}}{head[5]:<{w6}}')
#               print('-' * lines)
#               counter += 1
#              print(f"   {row['id']:<{w1}}{row['name']:<{w2}}{row['age']:<{w3}} {row['grade']:<{w4}} {row['subject_name']:<{w5}}{row['mark']:<{w6}}")
#              print('-' * lines)
# else:
#         search_id = int(input("შეიყვანეთ სტუდენტის ID: "))
#         with open(file_name, "r", newline='', encoding="utf-8") as csvfile:
#           reader = csv.DictReader(csvfile) 
#           for row in reader:
#                 if int(row['id']) == search_id:
#                     print("\nსტუდენტის ინფორმაცია:")
#                     print(row)
#                     found = True
#                 else:
#                     print("არასწორი'id'.")
#                     break


####################################################################################################
# დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.

# import os, csv
# path="files"
# file_name="students.csv"
# os.makedirs(path, exist_ok=True)
# def average_marks_by_subject(path="files", file_name="students.csv"):
#     file_name=os.path.join(path, file_name)
#     subject_marks = {}
#     with open(file_name, "r", newline='', encoding="utf-8") as csvfile:
#         reader = csv.DictReader(csvfile) 
#         for row in reader:
#             subject = row['subject_name']
#             try:
#                 mark = float(row['mark'])
#             except ValueError:
#                 continue  
            
#             if subject in subject_marks:
#                 subject_marks[subject].append(mark)
#             else:
#                 subject_marks[subject] = [mark]
                
#     print("\nსაშუალო შეფასება საგნების მიხედვით:")
#     for subject, marks in subject_marks.items():
#      average = sum(marks) / len(marks)
#      print(f"{subject}: {average:.2f}")
# average_marks_by_subject()

            
####################################################################################################
# დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. 
# მომხარებელი შეიყვანს სტუდენტის id, საგანს და განახლებულ ქულას.

# import os, csv
# path="files"
# file_name="students.csv"
# os.makedirs(path, exist_ok=True)
# def Update_mark(path="files", file_name="students.csv"):
#   file_name=os.path.join(path, file_name)
#   try:
#         student_id = int(input("შეიყვანეთ სტუდენტის ID: "))
#         subject_name = input("შეიყვანეთ საგნის სახელი: ")
#         new_mark = float(input("შეიყვანეთ განახლებული ქულა: "))
#   except ValueError:
#     print("გთხოვთ შეიყვანოთ ვალიდური მონაცემები (ID - მთელი რიცხვი, ქულა - ცალი წერტილი/ნამდვილ რიცხვი).")
#     return
#   updated = False
#   all_rows = []

#   with open(file_name, "r", newline='', encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             if int(row['id']) == student_id and row['subject_name'] == subject_name:
#                 row['mark'] = str(new_mark)
#                 updated = True
#             all_rows.append(row)

#   if not updated:
#         print(f"სტუდენტი ID={student_id} საგნით '{subject_name}' არ მოიძებნა.")
#         return
  
#   with open(file_name, "w", newline='', encoding="utf-8") as f:
#         fieldnames = ['id','name','age','grade','subject_name','mark']
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(all_rows)

#         print(f"სტუდენტის ID={student_id}, საგან '{subject_name}' ქულა განახლდა: {new_mark}")

# Update_mark()
