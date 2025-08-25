file=open("hassan.txt","r")
# Read the contents of the file
with open("hassan.txt", "r") as file:
    content = file.read()

# Modify the content (example: convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("hassan_modified.txt", "w") as new_file:
    new_file.write(modified_content)

# Print the contents of the new file
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