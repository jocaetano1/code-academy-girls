import abc

from domain.student_repository import StudentRepository


class Authentication(abc.ABC):

    @abc.abstractmethod
    def autenticate(self, *args, **kwargs):
        pass


class IdentityNumberAuth(Authentication):

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def autenticate(self, identity_number: str):
        student = self.repository.get(identity_number)
        return student
