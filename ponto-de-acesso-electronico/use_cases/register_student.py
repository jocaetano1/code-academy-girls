from domain.student_data_error import StudentDataError
from domain.student_repository import StudentRepository
from domain.student import Student
from shared.domain_error import DomainError


class StudentInvalidError(DomainError):
    def __init__(self, message: str):
        super().__init__(message)


class RegisterStudent:
    """Use case: Register a student in system."""

    def __init__(self, student_repository: StudentRepository):
        self.repository = student_repository

    def execute(self, data: dict):
        student = Student.compose(data)
        student_error = self.repository.create(student)
        if isinstance(student_error, StudentDataError):
            return student_error
        if isinstance(student_error, StudentInvalidError):
            return student_error
        return
