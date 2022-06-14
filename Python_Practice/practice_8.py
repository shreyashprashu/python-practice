import os
# Reading from a file
employee_file = open("employees.txt", "r")
print(employee_file.readable())
# print(employee_file.read())

for line in employee_file.readlines():
    print(line)

# print(employee_file.readlines())

# print(employee_file.readlines()[2])
employee_file.close()

# Appending to a file
# employee_file = open("employees.txt", "a")
# employee_file.write("\n ritesh -  customer service")
# employee_file.close()

# writing to a file

employee_file = open("employees1.txt", "w")
employee_file.write("shreyash - Data Engineer")
employee_file.close()

os.remove("employees1.txt")
