#copy file
import csv

with open('g:\\Documents\\Python_tmp\\train.csv') as source:
    s_lines=csv.reader(source)
    with open('g:\\Documents\\Python_tmp\\a.csv','w',newline='') as target:
        t_lines=csv.writer(target)
        t_lines.writerows(s_lines)


