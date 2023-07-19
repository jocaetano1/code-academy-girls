import abc
from domain.student import Student


class StudentRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, student: Student):
        pass

    @abc.abstractmethod
    def get(self, identity_number: str):
        pass

    @abc.abstractmethod
    def list(self):
        pass

    @abc.abstractmethod
    def count(self):
        pass
