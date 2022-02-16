teachers_timetable = [["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                      ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                      ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                      ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"],
                      ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"]]

teach = teachers
string = f"{teach}_timetable"
exec("%s = %d" % (string,))

print(teachers_timetable)
