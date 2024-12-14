name_of_files = input("Enter the name the files should have in common:")
number_of_files = int(input("Enter the number of files you want to create:"))
file_extension = input("Enter the file extension.")
for x in range(1,number_of_files+1):
    f = open(f"{name_of_files}-{x}.{file_extension}","x")