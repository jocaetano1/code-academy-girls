import unittest

from test_data.stubs.student_repository_stub import StudentRepositoryStub
from use_cases.register_student import RegisterStudent, StudentInvalidError
from domain.student_data_error import StudentDataError
from adaptors.inmem.inmem_student_repository import InmemStudentRepository


class RegisterStudentTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            "full_name": "Joao Santos",
            "identity_number": "004843261LA047",
            "course": "Curso de Introdução ao Python",
            "email": "john.doe@gmail.com",
            "phone_number": "+244933843893"
        }

    def test_register_student(self):
        """Deve registrar uma estudante"""
        repository = InmemStudentRepository()
        register_student = RegisterStudent(repository)
        register_student.execute(self.data)
        self.assertEqual(register_student.repository.count(), 1)

    def test_register_student_with_some_identity_number(self):
        """Deve retornar StudentInvalidError se o B.I for duplicado."""
        repository = StudentRepositoryStub()
        register_student = RegisterStudent(repository)
        error = register_student.execute(self.data)
        self.assertIsInstance(error, StudentInvalidError)

    def test_register_student_with_empty_data(self):
        """Deve retornar StudentDataError quando um dos campas estiver em branco."""
        data = {
            "full_name": "",
            "identity_number": "",
            "course": "",
            "email": "",
            "phone_number": ""
        }
        repository = InmemStudentRepository()
        register_student = RegisterStudent(repository)
        error = register_student.execute(data)
        self.assertIsInstance(error, StudentDataError)


if __name__ == "__main__":
    unittest.main()
