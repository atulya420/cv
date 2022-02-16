from prettytable import *
import random

def table(t):
    tb = PrettyTable(['1', '2', '3', '4', '5', '6'])
    tb.add_rows(t)
    print(tb)

def assign(section, teacher):
    n = 0
    for day in range(5):
        while n < 2:
                teacher_var_name = f"{teacher}_timetable"
                section_var_name = f"{section}_timetable"
                (globals()[section_var_name])[day][random.randint(0, 5)] = teacher
                n += 1


teachers_timetable = [["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                      ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                      ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                      ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                      ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"]]



class_timetable = [["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                   ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                   ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                   ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                   ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"]]

physics = ["Nidhi", "Jyoti", "Nupur", "Ripple"]
chemistry = ["Meenakshi", "Deepti", "Meenakshi", "Sutapa"]
mathematics = ["Sangeeta", "Anjali", "Deepti", "Sakshi"]
cs = ["Anuja", "Hema", "Promila", "Ruchi"]
activity = ["PE", "Art", "Chess"]
subjects = [physics, chemistry, mathematics, cs, activity]
sections = ['A', 'B', 'C', 'D']



for i in subjects:
    for j in i:
        var_name = f"{j}_timetable"
        globals()[var_name] = teachers_timetable.copy()

for i in sections:
        var_name = f"{i}_timetable"
        globals()[var_name] = class_timetable.copy()

for section in sections:
    l = [""]
    teacher = ""
    for subject in subjects:
        while teacher in l:
            teacher = random.choice(subject)
        l.append(teacher)
        assign(section, teacher)

table(A_timetable)
