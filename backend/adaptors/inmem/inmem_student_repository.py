from typing import Dict, Union

from domain.student import Student
from domain.student_data_error import StudentDataError
from domain.student_does_not_exist import StudentDoesNotExist
from domain.student_repository import StudentRepository
from use_cases.register_student import StudentInvalidError


class InmemStudentRepository(StudentRepository):
    """Repository of students in memory"""
    students: Dict[str, Student] = {}

    def create(self, student: Student) -> Union[Union[StudentInvalidError, StudentDataError]]:
        """Insert new student in database"""
        identity_number = student.identity_number
        if not student.is_valid():
            return StudentDataError("Dados estão incorrectos.")
        student_does_not_exist = self.get(identity_number)
        if isinstance(student_does_not_exist, StudentDoesNotExist):
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
