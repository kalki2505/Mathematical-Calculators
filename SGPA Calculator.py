def sgpa_calculator(grades, credits):
    sop = []
    for g in range(len(grades)):
        grades[g].upper()
        if grades[g] == "A+":
            sop += [4*credits[g]]
        elif grades[g] == "A":
            sop += [3.67*credits[g]]
        elif grades[g] == "A-":
                sop += [3.33 * credits[g]]
        elif grades[g] == "B+":
            sop += [3*credits[g]]
        elif grades[g] == "B":
            sop += [2.67*credits[g]]
        elif grades[g] == "B-":
            sop += [2.33*credits[g]]
        elif grades[g] == "C+":
            sop += [2*credits[g]]
        elif grades[g] == "C":
            sop += [1.67*credits[g]]
        elif grades[g] == "C-":
            sop += [1.33*credits[g]]
        elif grades[g] == "D":
            sop += [1 * credits[g]]
        elif grades[g] == "F":
            sop += [0]
        else:
            s = "Invalid grade"
            return False, s

    sgpa = sum(sop)/sum(credits)
    msg = "Your SGPA is "+ str(sgpa)
    return True, msg


print('\n\n\n\t\t\t ==>>  SGPA Calculator  <<==')
print('\n\n\t\tEnter total courses this semester:', end = ' ')
total_courses = int(input())
codes = []
grades = []
credits = []
for i in range(total_courses):
    print('\n\n\t\t\t>>> COURSE ',(i+1),' <<<')
    print('\n\tEnter course name code:', end=' ')
    codes += [str(input())]
    print('\n\tEnter course credits of ',codes[i],' :', end=' ')
    credits += [float(input())]
    print('\n\tEnter course grade of ', codes[i], ' :', end=' ')
    grades += [str(input())]

ret, msg = sgpa_calculator(grades, credits)
print('\n\n\t\t\tHey User! ',msg)
