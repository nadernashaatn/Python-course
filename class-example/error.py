import sys

file_name = 'recipes.txt'

try:
    my_file = open(file_name, 'x+')
    my_file.write('Meatballs\n')
    my_file.close()
except:
    print(f"The {file_name} file already exists")
