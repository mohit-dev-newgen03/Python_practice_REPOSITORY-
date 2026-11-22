# Tool 1 : User's age checking system

def get_age():
    while True:        
        try:
            users_age = int(input("Please give us your age sir: "))
            if users_age > 0:
                return f"Your age sir: {users_age}"
            print("Age must be positive!")
        except ValueError:
            print("Invalid value! Please provide your age in number")
        
print(get_age())


# Tool 2 : User's profile output 

def user_profile(name, city, skills):
    users_profile_dictionary = {}
    
    username = name.strip().title()
    usercity = city.strip().title()
    userskills = len(skills.split(","))
    usersrole = users_profile_dictionary.get("role", "intern")

    users_profile_dictionary["name"] = username
    users_profile_dictionary["city"] = usercity
    users_profile_dictionary["skills"] = userskills
    users_profile_dictionary["role"] = usersrole

    return users_profile_dictionary

user_name = input("What's your name sir ? ")
user_city = input("What's your cities name sir ? ")
user_skills = input("What are your skills sir ? ")

print(user_profile(user_name, user_city, user_skills))


# Tool 3 : Highest marks from the students list

def get_studentdata_list():
    students_data_list = []

    while True:
        student_name = input("Enter student name (or 'done'): ").strip().title()
        if student_name == "Done":
            break

        student_marks = float(input("Enter students marks: "))

        students_data_dict = {}
        students_data_dict["name"] = student_name
        students_data_dict["marks"] = student_marks
        students_data_list.append(students_data_dict)
        
    return students_data_list

def student_marks_calculator(student_list):
    if not student_list:
        return "No students registered!"

    topper_name = " " 
    highest_marks = -1
    for student in student_list:
        if student["marks"] > highest_marks:
            highest_marks = student["marks"]
            topper_name = student["name"]

    return f"Toppers name: {topper_name} and his highest marks: {highest_marks}"        

        
print(student_marks_calculator(get_studentdata_list()))