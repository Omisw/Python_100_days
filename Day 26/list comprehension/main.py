with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

list_file1 = [num.strip() for num in file_1_data]
list_file2 = [num.strip() for num in file_2_data]
result = [int(num) for num in list_file1 if num in list_file2]
# Write your code above 👆

print(result)
