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


# Second Tool :- Taxi charges calculator 

def calculate_fare_price (distance_km, ride_hour, ride_count):
    if distance_km <= 0:
        return "ERROR: Invalid Ride Details"
    elif not (0 <= ride_hour <= 23):
        return "ERROR: Invalid Ride Details"
    elif (ride_count < 1):
        return "ERROR: Invalid Ride Details"

    booking_fee = 3.00
    charges = 0

    if distance_km >= 20:
        charges = distance_km * 1.20
    elif  5 <= distance_km < 20:
        charges = distance_km * 1.50
    elif distance_km < 5:
        charges = distance_km * 2.00

    if (ride_hour >= 22) or (ride_hour <= 5):
        charges = charges + 8 

    if ride_count % 5 == 0:
        charges = charges * 0.90

    final_charge = charges + booking_fee
    return f"Total fare charges = {final_charge:.2f}" 
    


distance = float(input("What's the distance of your ride sir, please provide in K.M. ? "))
hour_of_day = int(input("What's the hour of the day is right now sir ? "))
ride = int(input("Which ride is this for you ? "))

print(calculate_fare_price(distance, hour_of_day, ride)) 