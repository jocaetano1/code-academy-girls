import unittest


from use_cases.auth.identity_number import IdentityNumberAuthentication
from test_data.stubs.student_repository_stub import StudentRepositoryStub
from domain.student_does_not_exist import StudentDoesNotExist
# from domain.student import Student


class PointAuthenticationTestCase(unittest.TestCase):
    def test_point_authentication_by_identity_number(self):
        """Deve autenticar a estudande por meio do seu número do B.I"""
        # Arrange
        identity_number = "004843261LA047"
        repository = StudentRepositoryStub()
        identity_number_auth = IdentityNumberAuthentication(repository)
        # Act.
        student = identity_number_auth.autenticate(identity_number)
        # Assert
        self.assertIsNotNone(student)
        self.assertEqual(student.identity_number, identity_number)

    def test_point_authentication_when_identity_number_not_exist(self):
        """Deve retorna StudentDoesNotExist quando o B.I não existe no sistema."""
        # Arrange
        identity_number = "004843261LA040"
        repository = StudentRepositoryStub()
        identity_number_auth = IdentityNumberAuthentication(repository)
        # Act.
        error = identity_number_auth.autenticate(identity_number)
        # Assert
        self.assertIsNotNone(error)
        self.assertIsInstance(error, StudentDoesNotExist)



