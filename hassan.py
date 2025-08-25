file=open("hassan.txt","r")

with open("hassan.txt", "r") as file:
    content = file.read()


modified_content = content.upper()


with open("hassan_modified.txt", "w") as new_file:
    new_file.write(modified_content)


with open("hassan_modified.txt", "r") as new_file:
    print(new_file.read())
filename = input("Enter the filename to read: ")
try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist.")
except IOError:

    print("Error: Cannot read the file.")
