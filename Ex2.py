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

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_given = 0
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviews_given = []

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached.append('Python')

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

lecturer = Lecturer('John', 'Doe')
lecturer.courses_attached.append('Python')

best_student.rate_lecture(lecturer, 'Python', 8)
best_student.rate_lecture(lecturer, 'Python', 9)

print(lecturer.grades)
