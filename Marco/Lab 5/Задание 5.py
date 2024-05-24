school = {
    '1а': 43, '1б': 35, '1в': 28, '2а': 34, '2и': 21, '3б': 24, '4а': 27, '5а': 20, '6в': 17, '7и': 21}


def change(team, new):
    school[team] = new


def add(team, num):
    school[team] = num


def remove(team):
    if team in school:
        total_students = school.pop(team)
        remain = len(school)
        arg = total_students // remain
        for i in school:
            school[i] += arg


def data():
    all_st = sum(school.values())
    all_classes = len(school)
    students = {i: students for i, students in school.items()}
    return all_st, all_classes, students


change('1б', 29)
add('10с', 22)
remove('1а')
print(data())
