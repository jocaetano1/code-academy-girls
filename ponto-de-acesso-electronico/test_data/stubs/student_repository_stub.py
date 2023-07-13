from typing import Dict, Union

from domain.student import Student
from domain.student_data_error import StudentDataError
from domain.student_does_not_exist import StudentDoesNotExist
from domain.student_repository import StudentRepository
from use_cases.register_student import StudentInvalidError


class StudentRepositoryStub(StudentRepository):
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self._populate()

    def _populate(self):
        data = {
            "full_name": "Joao Santos",
            "identity_number": "004843261LA047",
            "course": "Curso de Introdução ao Python",
            "email": "john.doe@gmail.com",
            "phone_number": "+244933843893"
        }
        student = Student.compose(data)
        self.create(student)

    def create(self, student: Student) -> Union[Union[StudentInvalidError, StudentDataError]]:
        """Insert new student in database"""
        if not student.is_valid():
            return StudentDataError("Dados estão incorrectos.")
        student_or_error = self.get(student.identity_number)
        if isinstance(student_or_error, StudentDoesNotExist):
            self.students[student.identity_number] = student
        return StudentInvalidError("Identity Number has been registred.")

    def count(self):
        """Count a quantity of student in database."""
        return len(self.students)

    def get(self, identity_number: str) -> Union[StudentDoesNotExist, Student]:
        """Retrive a student."""
        student = self.students.get(identity_number)
        if not student:
            return StudentDoesNotExist("Student does not exist.")
        return student

    def list(self):
        """List all student."""
        return self.students
