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