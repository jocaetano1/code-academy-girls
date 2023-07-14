import abc

from domain.student_repository import StudentRepository


class Authentication(abc.ABC):

    @abc.abstractmethod
    def autenticate(self, *args, **kwargs):
        pass
