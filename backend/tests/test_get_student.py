import unittest

from adaptors.inmem.inmem_student_repository import InmemStudentRepository
from domain.student_does_not_exist import StudentDoesNotExist
from test_data.stubs.student_repository_stub import StudentRepositoryStub
from use_cases.get_student import GetStudent


class GetStudentTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.identity_number = "004843261LA047"

    def test_get_student_with_identity_number(self):
        """Deve retornar a estudante registrada no sistema."""
        repository = StudentRepositoryStub()
        get_student = GetStudent(repository)
        student = get_student.execute(self.identity_number)
        self.assertEqual(student.identity_number, self.identity_number)

    def test_get_student_does_not_exists(self):
        """Deve retornar erro quando tenta buscar uma estudante que não existe."""
        repository = InmemStudentRepository()
        get_student = GetStudent(repository)
        error = get_student.execute(self.identity_number)
        self.assertIsInstance(error, StudentDoesNotExist)
