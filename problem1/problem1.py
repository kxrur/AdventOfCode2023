import os
import math

relative_path = os.path.join(os.path.dirname(__file__), 'test.txt')

def find_first_num(line: str, num: int ) -> int:
    for char in line:
        if not is_num(char) and num != 0:
            return num
        elif is_num(char):
            new_num = give_value(num, int(char))
            new_line = line[1:]
            return find_first_num(new_line, new_num)
    return -1

def find_last_num(line:str, num:int)->int:
    for i in range(len(line)-1,0,-1):
        if not is_num(line[i]) and num !=0:
            return num
        elif is_num(line[i]):
            new_num = give_value(num, int(line[i]))
            new_line = line[:-1]
            return find_last_num(new_line, new_num)
    return -1

def is_num(c: str)->bool:
    return ord(c) > 47 and ord(c) < 58

def give_value(value:int, to_add:int)->int:
    #this is unecessary when adding values 1 by 1 (what I do), but cool if the 'to_add' where 5 digits long
    value = value*(10**(math.ceil(math.log10(to_add))))+to_add
    return value

sum = 0

with open(relative_path, 'r') as file:
    for line in file:
        firs_num = find_first_num(line, 0)
        last_num = find_last_num(line,0)
        value = give_value(firs_num,last_num)
        sum+=value 



"""
        for char in line:
            if ord(char) > 47 and ord(char) < 58:
                value = int(char)
                break
        for i in range(len(line)-1,0,-1):
            if ord(line[i]) > 47 and ord(line[i]) < 58:
                last = int(line[i])
                value = value*(10**(math.ceil(math.log10(last))))+last
                break
        sum+=value
        """

print("The sum is: " + str(sum))


