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


# Tool 4 : Giving user its server name and port number 

import sys
import random


if len(sys.argv) == 1:
    sys.exit("Usage: python server_assign.py <your_name>")
elif len(sys.argv) > 2:
    sys.exit("Error: Please provide only single word name or wrap in quotes")

server_name = random.choice(["AWS-US-East", "AWS-EU-Central", "GCP-Asia-South"])
port_number = random.randint(1000, 9999)

print(f"Assigned Server for {sys.argv[1]}: {server_name}:{port_number}")


# Tool 5 : Using API for first time, Cat facts and there length

import sys
import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

if response.status_code != 200:
    sys.exit(f"API Error! Server returned status: {response.status_code}")

data = response.json()
cat_fact = data["fact"]
length = data["length"]
catagory = ""

if length < 80 :
    catagory = "[QUICK READ]"
else:
    catagory = "[DETAILED READ]"

print(f"Category: {catagory}")
print(f"Facts: {cat_fact}")
print(f"Length: {length}")    