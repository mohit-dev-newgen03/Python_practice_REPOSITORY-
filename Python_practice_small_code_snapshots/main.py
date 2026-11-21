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