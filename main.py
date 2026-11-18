# First tool :- File approval system according to extension and size.

def file_access(file, size):
    file_name = file.strip().lower()

    if file_name.endswith(".exe"):
        return "BLOCKED: Executables are not allowed!"
    elif file_name.endswith((".pdf", ".png")):
        if size > 2048:
            return "REJECTED: File exceeds 2048 KB limit"
        else:
            return f"ACCEPTED: Valid {file_name}"
    else:
        return "ERROR: Unsupported file format"

filename = input("what's your file name ? ")
filesize = float(input("what's your file size ? "))    

print(file_access(filename, filesize))


# Second Tool :- E-Commerce web billing and discount app 

def bill_calculate(amount, day):
    if amount <= 0:
        return "!ERROR: Invalid Input"
    elif 1 >= day >= 31:
        return "!ERROR: Invalid Input"
    elif amount >= 5000:
        discount = amount * (20 // 100)
        final_amount = amount - discount
        
        if day % 2 == 0:
            return f"your wihtout discounted amount :{amount} and final discounted amount :{50 - final_amount}"
        else:
            return f"your wihtout discounted amount :{amount} and final discounted amount :{final_amount}"  
    elif 1000 >= amount <= 4999:
        discount = amount * (10 // 100)
        final_amount = amount - discount
        
        if day % 2 == 0:
            return f"your wihtout discounted amount :{amount} and final discounted amount :{50 - final_amount}"
        else:
            return f"your wihtout discounted amount :{amount} and final discounted amount :{final_amount}" 
    elif amount <= 1000:
        return f"there is not any discountso at this price your final billing price is :{amount}"

undiscounted_amount = float(input("Sir please give us your billing price: "))
day_of_purchasing = input("What's day today sir ? ")

print(bill_calculate(undiscounted_amount, day_of_purchasing))