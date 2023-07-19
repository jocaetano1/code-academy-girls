from domain.student_repository import StudentRepository


class ListStudent:

    def __init__(self, student_repository: StudentRepository):
        self.repository = student_repository

    def execute(self):
        students = self.repository.list()
        return list(students.values())
