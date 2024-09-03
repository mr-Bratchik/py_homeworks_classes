class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course].append(grade)
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_grades = 0
        total_grades = 0
        for all_grades in self.grades.values():
            sum_grades += sum(all_grades)
            total_grades += len(all_grades)

        return sum_grades / total_grades if total_grades != 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_pr = ', '.join(self.courses_in_progress)
        fin_d_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_pr}\n'
                f'Завершенные курсы: {fin_d_courses}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        sum_grades = 0
        total_grades = 0
        for all_grades in self.grades.values():
            sum_grades += sum(all_grades)
            total_grades += len(all_grades)

        return sum_grades / total_grades if total_grades != 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade:.1f}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


student_1 = Student('Aleksander', 'Bratchik', 'male')
student_1.courses_in_progress.append('Python')
student_1.finished_courses.append('Git')
student_1.grades = {'Python': [9, 10, 8]}

student_2 = Student('Olga', 'Marina', 'female')
student_2.courses_in_progress.append('Java')
student_2.finished_courses.append('Git')
student_2.grades = {'Java': [10, 10, 8]}

lecturer_1 = Lecturer('Magnus', 'Carlson')
lecturer_1.courses_attached.append('Python')
lecturer_1.grades = {'Python': [10, 9, 10]}

lecturer_2 = Lecturer('Garry', 'Kasparov')
lecturer_2.courses_attached.append('C#')
lecturer_2.grades = {'C#': [10, 10, 10]}

reviewer_1 = Reviewer('Jan', 'Nepomnyashchy')
reviewer_1.courses_attached.append('Java')
reviewer_1.grades = {'Java': [10, 9, 9]}

print(student_1)
print(lecturer_1)
print(reviewer_1)
print(student_1 < student_2)
print(lecturer_1 > lecturer_2)