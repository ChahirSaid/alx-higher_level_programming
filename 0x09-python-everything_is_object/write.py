string = input("Enter the string: ")
filename = input("Enter the filename: ")

with open(filename, 'w') as file:
    file.write(str(string))
