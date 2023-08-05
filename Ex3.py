class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if course in self.courses_in_progress and isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]

    def give_lecture(self, lecturer, course):
        if course in self.courses_in_progress and isinstance(lecturer, Lecturer):
            lecturer.lectures_given += 1

    def __str__(self):
        return f"Студент:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calculate_average_grade()}\n" \
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
            f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def calculate_average_grade(self):
        total_grades = 0
        subjects = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            subjects += len(grades)
        if subjects > 0:
            return round(total_grades / subjects, 2)
        else:
            return "Нет оценок"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Ментор:\nИмя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_given = 0
        self.grades = {}

    def __str__(self):
        return f"Лектор:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calculate_average_grade()}"

    def calculate_average_grade(self):
        total_grades = 0
        subjects = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            subjects += len(grades)
        if subjects > 0:
            return round(total_grades / subjects, 2)
        else:
            return "Нет оценок"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviews_given = []

    def __str__(self):
        return f"Проверяющий:\nИмя: {self.name}\nФамилия: {self.surname}"

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')
best_student.finished_courses.append('Введение в программирование')

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached.append('Python')

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached.append('Python')

best_student.rate_lecture(lecturer, 'Python', 8)
best_student.rate_lecture(lecturer, 'Python', 9)

print(cool_mentor)
print(lecturer)
print(best_student)