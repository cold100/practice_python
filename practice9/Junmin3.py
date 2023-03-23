# 3. Деканат.
# Дано: список студентов: каждый элемент списка содержит фамилию,
# имя, отчество, год рождения, курс, номер группы, оценки по пяти предметам.
#
# Задание: реализуйте сл. функции:
#
# 1) возвращает список студентов по курсу, причем студенты одного курса располагались в алфавитном порядке;
# 2) находит средний балл каждой группы по каждому предмету;
# 3) определяет самого старшего студента и самого младшего студента.
# 4) возвращает словарь, где для каждой группы определен лучший с точки зрения успеваемости студент.

def get_students_by_course(students):
    course = int(input('Course number: '))
    course_students = []
    for student in students:
        if student[4] == course:
            course_students.append(student)
    return sorted(course_students)


def get_avg_scores_by_group(students):
    groups_marks = {}
    for student in students:
        group = student[5]
        grade = student[6:]
        if group in groups_marks:
            grade_sum = list(map(lambda x, y: x + y, grade, groups_marks[group][0]))
            stud_number = groups_marks[group][1]
            groups_marks[group] = [grade_sum, stud_number + 1]
        else:
            groups_marks[group] = [grade, 1]

    for i, j in groups_marks.items():
        j = list(map(lambda x, y=j[1]: x / y, j[0]))
        groups_marks[i] = j

    return groups_marks


def get_oldest_and_young_student(students):
    young = max(students, key=lambda s: s[3])
    old = min(students, key=lambda s: s[3])
    return young, old



def get_best_student_of_group(students):
    best_students = {}

    for stud in students:
        group = stud[5]
        grade = stud[6:]
        student = stud[:3]
        if group in best_students.keys():
            if sum(best_students[group][1]) < sum(grade):
                best_students[group] = [student, grade]
        else:
            best_students[group] = [student, grade]
    return best_students



students = [
    ('Ivanov', 'Ivan', 'Ivanovich', 1999, 2, '101', 4, 5, 3, 3, 4),
    ('Petrov', 'Petr', 'Petrovich', 2002, 1, '102', 3, 4, 4, 3, 5),
    ('Sidorov', 'Sidor', 'Sidorovich', 2000, 3, '103', 5, 5, 5, 5, 5),
    ('Sergeev', 'Sergey', 'Sergeevich', 2002, 2, '101', 4, 4, 4, 4, 4),
    ('Victorov', 'Victor', 'Victorovich', 2003, 1, '102', 4, 5, 5, 4, 5),
    ('Andreev', 'Andrey', 'Andreevich', 2004, 3, '103', 3, 4, 3, 3, 3),
]

print("1) Возвращает список студентов по курсу, причем студенты одного курса располагались в алфавитном порядке.\n"
      "2) Находит средний балл каждой группы по каждому предмету.\n"
      "3) Определяет самого старшего студента и самого младшего студентов.\n"
      "4) Возвращает словарь, где для каждой группы определен лучший с точки зрения успеваемости студент.\n")
num_var = int(input("Введите номер задания: "))
match num_var:
    case 1:
        result = get_students_by_course(students)
        for stud in result:
            print(stud)

    case 2:
        result = get_avg_scores_by_group(students)
        for gr, grade in result.items():
            print(f'Group - {gr} Grade - {grade}')

    case 3:
        result = get_oldest_and_young_student(students)
        print(f'Young - {result[0]},\nOld - {result[1]}')

    case 4:
        result = get_best_student_of_group(students)
        for stud in result:
            print(f'Group - {stud}, Name - {result[stud]}')

    case _:
        print('Этого номера нет')
