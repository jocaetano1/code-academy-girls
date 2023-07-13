from shared.domain_error import DomainError


class StudentDoesNotExist(DomainError):
    def __init__(self, message: str):
        super().__init__(message)