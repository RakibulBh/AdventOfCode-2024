import re

multiplications = []
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

res = 0

with open('day3/day3.txt', 'r') as file:
    for line in file:
        vals = re.findall(pattern, line.strip())
        for (num1, num2) in vals:
            print("Num1: ", num1, " Num2: ", num2)
            res += int(num1) * int(num2)

print(res)
        