
filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
