n = int(input("Enter number of students: "))
students = []

for _ in range(n):
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    grade = int(input("Enter grade: "))
    students.append((name, age, grade))

sorted_students = sorted(students, key=lambda x: x[2])  # Sort by grade
print("Sorted Student Records:", sorted_students)
