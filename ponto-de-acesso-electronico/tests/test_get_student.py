import unittest

from domain.student_repository import StudentRepository
from test_data.stubs.student_register_stub import StudentRegisterRepositoryStub


class GetStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, identity_number: str):
        return self.repository.get(identity_number)


class GetStudentTestCase(unittest.TestCase):

    def test_get_student_with_identity_number(self):
        """Deve retornar o estudante registrado no sistema."""
        identity_number = "004843261LA047"
        repository = StudentRegisterRepositoryStub()
        get_student = GetStudent(repository)
        student = get_student.execute(identity_number)
        self.assertEqual(student.identity_number, identity_number)
