from domain.student_repository import StudentRepository

class GetStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, identity_number: str):
        return self.repository.get(identity_number)