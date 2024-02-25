student = {}
number_of_student = int(input("Number of Student : "))

for i in range(number_of_student) :
    name = str(input("Input name : "))
    grade = int(input(f"Input grade for {name} : "))
    
    student[name] = grade

print(student)