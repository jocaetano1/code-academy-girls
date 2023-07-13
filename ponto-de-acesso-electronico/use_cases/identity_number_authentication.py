class IdentityNumberAuth(Authentication):

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def autenticate(self, identity_number):
        student = self.repository.get(identity_number)
        return student
