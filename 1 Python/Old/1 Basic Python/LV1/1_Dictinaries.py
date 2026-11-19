School_Grades = {
    "Mark": 92,
    "Henry": 82,
    "John": 85,
    "Alice": 74,
    "Teddy": 78,
    "Karen": 95,
    "Josh": 67,
    "Anna": 56,
    "Olivia": "Unattended",
    "Mia": "Unattended",
    "Evan": -75  # This is an error made by the teacher
}


print("This is a system to check a student's grade for the test,")
Student = input("please input the student's name: ")

try:
    if School_Grades.get(Student) == "Unattended":
        print("The student has not attended this test for other reasons,")
        print("the student doesn't receive a grade for this test.") + exit()
    else:
        print(Student + "'s math grades is " + str(School_Grades[Student]) + "%,")

    if 90 <= School_Grades[Student] <= 100:
        print("the student scores an A.")
    elif 80 <= School_Grades[Student] < 90:
        print("the student scores a B.")
    elif 70 <= School_Grades[Student] < 80:
        print("the student scores a C.")
    elif 60 <= School_Grades[Student] < 70:
        print("the student scores a D.")
    elif 0 <= School_Grades[Student] < 60:
        print("the student scores a F.")
    else:
        print("the student's grades are incorrect, please recheck the system.")
except KeyError:
    print("The student name is not found in the system.")
