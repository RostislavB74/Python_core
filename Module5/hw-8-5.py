grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    def new_grade(values_students):
        el1 = 0
        for keys, values in grades.items():
            if values_students == keys:
                el1 = values

            # print(el1)

        return el1

    el = []
    # el1 = []
    for keys_students, values_students, in students.items():
        # print(keys_students, values_students)
        el.append('|{:<10}|{:^5}|{:^5}|'.format(keys_students,
                  values_students, new_grade(values_students)))

    return el
# for count in range(len(students)):
#    print('{:>4}|{:<10}|{:^5}|{:^5}\n'.format(
#        count, students[count], students, grades[students.values]))
# for keys_students, values_students, in enumerate(students, start=1):
    #   el = '{:>4}|{:<10}|'.format(keys_students, values_students)

    # el = ["   1|Nick      |  A  |  5  ", "   2|Olga      |  B  |  5  ",
    #     "   3|Mike      |  FX |  2  ", "   4|Anna      |  C  |  4  "]


for el in formatted_grades(students):
    print(el)
# el = formatted_grades(students)
# rint(el)

# for keys_students, values_students, in enumerate(students, start=1):"#
#    for keys, values, in grades.items():
#        if keys in values_students:
#            keys = values_students

#            print('{:>4}|{:<10}|{:^5}|{:^5}'.format(keys_students,
#                 values_students, grades[keys], grades[values]))
#      else:
#
