from dataclasses import dataclass


@dataclass(init=False)
class Student:
    full_name: str
    identity_number: str
    course: str
    email: str
    phone_number: str

    @staticmethod
    def compose(data: dict):
        student = Student()
        student.full_name = data.get("full_name")
        student.identity_number = data.get("identity_number")
        student.course = data.get("course")
        student.email = data.get("email")
        student.phone_number = data.get("phone_number")
        return student

    def is_valid(self) -> bool:
        return len(self.full_name) > 0 \
            and len(self.identity_number) > 0 \
            and len(self.course) > 0 \
            and len(self.email) > 0 \
            and len(self.phone_number) > 0


