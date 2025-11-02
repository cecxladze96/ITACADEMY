
my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}

print("სტუდენტების ID-ს სია:")
for student in my_dict["students"]:
    print(f"- {student['id']}")

student_id = int(input("\nშეიყვანეთ სტუდენტის ID: "))
selected_student = None
for student in my_dict["students"]:
    if student["id"] == student_id:
        selected_student = student
        break

if selected_student:
    print(f"\nსტუდენტის მონაცემები:")
    print(f"სახელი: {selected_student['name']}")
    print(f"ასაკი: {selected_student['age']}")

    print("\nქულები საგნებით:")
    for subject in my_dict["subjects"]:
        grade = subject["grades"].get(str(student_id), "N/A") 
        print(f"{subject['name']}: {grade}")
else:
    print("სტუდენტი ამ ID-ით ვერ მოიძებნა.")