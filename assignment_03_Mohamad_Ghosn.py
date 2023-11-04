student_data = [
    {
        "ID": 1,
        "Name": "Ali",
        "Age": 20,
        "Major": "Computer Science",
        "GPA": 3.7
    },
    {
        "ID": 2,
        "Name": "Bob",
        "Age": 21,
        "Major": "Engineering",
        "GPA": 3.9
    }
]

def get_student_by_id(data, student_id):   #If it exists, return its data
    for student in data:
        if student["ID"] == student_id:
            return student
    return None     #Or nothing

def get_all_students(data): #everything
    return data

def get_students_by_major(data, major): #To return information according to major
    students = []
    for student in data:
        if student["Major"] == major:
            students.append(student)
    return students

def add_student(data, student): #add student informations
    data.append(student)

def find_common_majors(data):  #same major
    majors = {}
    for student in data:
        major = student["Major"]
        if major in majors:
            majors[major] += 1
        else:
            majors[major] = 1
    common_majors = []
    for major, count in majors.items():
        if count > 1:
            common_majors.append(major)
    return common_majors

def delete_student(data, student_id): #remove student
    for student in data:
        if student["ID"] == student_id:
            data.remove(student)
            return True
    return False

def calculate_average_gpa(data):  #GPA Based on data
    total_gpa = 0
    for student in data:
        total_gpa += student["GPA"]
    if len(data) > 0:
        average_gpa = total_gpa / len(data)
        return average_gpa
    else:
        return None

def get_top_performers(data, n):  #best performers
    sorted_students = sorted(data, key=lambda x: x["GPA"], reverse=True)
    return sorted_students[:n]

def main():
    while True:
        print("1. Get Student by ID")
        print("2. Get All Students")
        print("3. Get Students by Major")
        print("4. Add Student")
        print("5. Find Common Majors")
        print("6. Delete Student")
        print("7. Calculate Average GPA")
        print("8. Get Top Performers")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            student_id = int(input("Enter student ID: "))
            student = get_student_by_id(student_data, student_id)
            if student:
                print("Student found:")
                print(student)
            else:
                print("Student not found.")
        
        elif choice == 2:
            students = get_all_students(student_data)
            print("All students:")
            for student in students:
                print(student)
        
        elif choice == 3:
            major = input("Enter major: ")
            students = get_students_by_major(student_data, major)
            if students:
                print("Students in", major, "major:")
                for student in students:
                    print(student)
            else:
                print("No students found in", major, "major.")
        
        elif choice == 4:
            max_id = max([student["ID"] for student in student_data])
            new_id = max_id + 1
            student = {}
            student["ID"] = new_id
            student["Name"] = input("Enter student name: ")
            student["Age"] = int(input("Enter student age: "))
            student["Major"] = input("Enter student major: ")
            student["GPA"] = float(input("Enter student GPA: "))
            student_data.append(student)
            print("Student added successfully.")
        elif choice == 5:
            common_majors = find_common_majors(student_data)
            if common_majors:
                print("Common majors:")
                for major in common_majors:
                    print(major)
            else:
                print("No common majors found.")
        
        elif choice == 6:
            student_id = int(input("Enter student ID: "))
            if delete_student(student_data, student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        
        elif choice == 7:
            average_gpa = calculate_average_gpa(student_data)
            if average_gpa:
                print("Average GPA:", average_gpa)
            else:
                print("No students found.")
        
        elif choice == 8:
            n = int(input("Enter number of top performers: "))
            top_performers = get_top_performers(student_data, n)
            print("Top performers:")
            for student in top_performers:
                print(student)
        
        elif choice == 9:
            print("Exiting program ,")
            print("Thank you, Georgio, and thank you, SE Factory")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()