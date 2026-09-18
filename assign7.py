#syntax
file = open("students.txt", "r")

data = file.read()

print(data)

file.close()
with open("students.txt", "r") as file:
    line = file.readline()
    print(line)
    line1 = file.readline()
line2 = file.readline() 
output = open("output.txt", "w")

for line in first_two_lines:
    output.write(line)

output.close()

print("First two lines have been written to output.txt")