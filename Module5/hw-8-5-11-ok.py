grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):

    def new_grade(values_students):

        el1 = 0
        for keys, values in grades.items():
            if values_students == keys:
                el1 = values

        return el1

    el = []
    index = 1
    for keys_students, values_students, in students.items():

        el.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(index, keys_students,
                  values_students, new_grade(values_students)))
        index += 1
    # print(el)
    return el


for el in formatted_grades(students):
    print(el)
