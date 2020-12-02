import os

f = open(os.path.realpath('adventOfCode/day1_numbercrunching/numbers'), 'r')

line_content = f.read()
line_number = line_content.split('\n')

for line in line_number:
    if int(len(line)) == 0:
        break
    for line2 in line_number:
        if int(len(line2)) == 0:
            break
        for line3 in line_number:
            if int(len(line3)) == 0:
                break
            if int(line) + int(line2) + int(line3) == 2020:
                print(line, line2, line3)
                print(int(line)*int(line2)*int(line3))
