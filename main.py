# def average_grade(member):
#     average = float(0)
#     sum_grades = int(0)
#     quantity_grades = int(0)
#     for grades in member.grades.values():
#         quantity_grades += len(grades)
#         sum_grades += sum(grades)
#         # print(grades, '\n', quantity_grades, sum_grades)
#     average = sum_grades / quantity_grades
#     return average

# def average_grade_course(members_list, course_name):
#     average = float(0)
#     sum_grades = int(0)
#     quantity_grades = int(0)
#     for member in members_list:
#         for course in member.grades.keys():
#             if course == course_name:
#                 # print(course)
#                 quantity_grades += len(member.grades[course])
#                 sum_grades += sum(member.grades[course])
#                 # print(quantity_grades, sum_grades)
#     average = sum_grades/quantity_grades
#     return average

def average_grade_course(members_list, course_name):
    if not isinstance(members_list, list) or len(members_list) == 0:
        return "Нет списка"
    else:
        grades_list = []
        for member in members_list:
            grades_list.extend(member.grades.get(course_name, []))
            # print(grades_list)
    if len(grades_list) == 0:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(grades_list) / len(grades_list), 2)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(grade, int) and 1 <= grade <= 10 and isinstance(lecturer,
                                                                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка за домашние задания: ' + str(
            average_grade(self)) + '\n' + 'Курсы в процессе изучения: ' + str(', '.join(self.courses_in_progress)) + '\n' + 'Завершенные курсы: ' + str(', '.join(self.finished_courses))
        return res

    def average_grade(self):
        if not self.grades:
            return 0
        else:
            grades_list = []
            for grade in self.grades.values():
                grades_list.extend(grade)
                # print(grades_list)
        return round(sum(grades_list) / len(grades_list), 2)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('Разные категории')
        else:
            return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('Разные категории')
        else:
            return self.average_grade < other.average_grade

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('Разные категории')
        else:
            return self.average_grade <= other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        #     self.name = name
        #     self.surname = surname
        #     self.courses_attached = []
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        # average = average_grade(self)
        res = 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка за лекции: ' + str(
            average_grade(self))
        return res

    def average_grade(self):
        if not self.grades:
            return 0
        else:
            grades_list = []
            for grade in self.grades.values():
                grades_list.extend(grade)
                # print(grades_list)
        return round(sum(grades_list) / len(grades_list), 2)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('Разные категории')
        else:
            return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('Разные категории')
        else:
            return self.average_grade < other.average_grade

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('Разные категории')
        else:
            return self.average_grade <= other.average_grade


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(grade, int) and 1 <= grade <= 10 and isinstance(student,
                                                                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.add_finished_courses('Введение в программирование')
best_student1 = Student('Ruoy1', 'Eman1', 'your_gender')

# cool_mentor = Mentor('Some', 'Buddy1')
# cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 6)
# cool_mentor.rate_hw(best_student, 'Git', 5)

# print(best_student.grades)

best_student.courses_in_progress += ['Git']
best_student.grades['Git'] = [10, 10, 5, 5]
best_student.grades['Python'] = [5, 10]
best_student1.grades['Git'] = [5, 10, 10, 10]
# best_student1.grades['Python'] = [5, 5, 10]

# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
print(best_student.average_grade())
print(best_student1.average_grade())
print(best_student.average_grade() < best_student1.average_grade())

# print(cool_mentor.courses_attached)

cool_lecturer = Lecturer('Some_lecturer', 'Buddy2')
cool_lecturer.courses_attached += ['Git']
cool_lecturer.courses_attached += ['Python']

cool_lecturer1 = Lecturer('Some_lecturer1', 'Buddy2')
cool_lecturer1.courses_attached += ['Python']
cool_lecturer1.grades['Python'] = [5, 10]
cool_lecturer1.grades['Git'] = [5, 10, 5, 10]

best_student.rate_hw(cool_lecturer, 'Git', 9)
best_student.rate_hw(cool_lecturer, 'Git', 8)
# print(best_student.rate_hw(cool_lecturer, 'Python', '1.1'))
# print(best_student.rate_hw(cool_lecturer, 'G', 8))
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 5)
# print(best_student.__dict__)
# print(cool_lecturer.__dict__)

# print(cool_lecturer1.__dict__)
print(cool_lecturer.average_grade())
print(cool_lecturer1.average_grade())
print(cool_lecturer.average_grade() > cool_lecturer1.average_grade())
print(cool_lecturer1.average_grade() < best_student.average_grade())
print(cool_lecturer1.__class__)
print(best_student.__class__)
print(not isinstance(cool_lecturer1, best_student.__class__))

cool_reviewer = Reviewer('Some_reviewer', 'Buddy3')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Python', 3)
# print(cool_reviewer.rate_hw(best_student, 'Git', 2))
# print (cool_reviewer.rate_hw(best_student, 'G', 1))
# print(best_student.__dict__)

# print(cool_reviewer.__dict__)
# print(cool_reviewer)
# print(cool_lecturer.__dict__)
# print(cool_lecturer)
# print(best_student.__dict__)
# print(best_student)

# print(best_student.__dict__)
# print(best_student1.__dict__)
# print ('Средняя оценка студентов за курс: Python', average_grade_course([best_student, best_student1], 'Python'))
# print ('Средняя оценка студентов за курс: Git:', average_grade_course([best_student, best_student1], 'Git'))
# print ('Средняя оценка студентов за курс: Git:', average_grade_course([], 'Git'))
# print ('Средняя оценка студентов за курс: Python', average_grade_course([best_student1], 'Python'))

# print(cool_lecturer.__dict__)
# print(cool_lecturer1.__dict__)
# print ('Средняя оценка лекторов за курс: Python', average_grade_course([cool_lecturer, cool_lecturer1], 'Python'))
# print ('Средняя оценка лекторов за курс: Git', average_grade_course([cool_lecturer, cool_lecturer1], 'Git'))