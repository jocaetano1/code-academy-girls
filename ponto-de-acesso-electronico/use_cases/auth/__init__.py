import abc


class Authentication(abc.ABC):

    @abc.abstractmethod
    def autenticate(self, *args, **kwargs):
        pass
