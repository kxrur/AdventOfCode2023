import os

relative_path = os.path.join(os.path.dirname(__file__), 'data.txt')

def find_first_num(line: str, num:str)->str:
    for char in line:
        if char.isdigit():
            num += char
            return num
        line = line[1:] 
    return num

def find_last_num(line: str, num:str)->str:
    for i in range(len(line)-1,-1,-1):
        char = line[i]
        if char.isdigit():
            num += char
            return num
        line = line[:-1] 
    return num

sum = 0
with open(relative_path, 'r') as file:
    for line in file:
        local_value = 0
        line = line.rstrip('\n')
        first_num = find_first_num(line, "")
        last_num = find_last_num(line,"")
        value_str = first_num+last_num
        local_value = int(value_str)
        sum+=local_value 

print("The sum is: " + str(sum))

