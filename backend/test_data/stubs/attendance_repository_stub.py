from typing import List

from domain.attendance_repository import AttendanceRepository
from domain.attendance import Attendance
from domain.student import Student


class AttendanceRepositoryStub(AttendanceRepository):
    attendances: List[Attendance] = []

    def __init__(self):
        self._populate()

    def _populate(self):
        student_data_1 = {
            "full_name": "Joao Santos",
            "identity_number": "004843261LA047",
            "course": "Curso de Introdução ao Python",
            "email": "joao.santos@gmail.com",
            "phone_number": "+244933843893"
        }

        student_data_2 = {
            "full_name": "John Doe",
            "identity_number": "004843261LA048",
            "course": "Curso de Introdução ao Python",
            "email": "john.doe@gmail.com",
            "phone_number": "+244933843890"
        }

        student_1 = Student.compose(student_data_1)
        attendance_1 = Attendance.compose(student_1)
        attendance_1.assign_entry_time()

        student_2 = Student.compose(student_data_2)
        attendance_2 = Attendance.compose(student_2)
        attendance_2.assign_entry_time()
        attendance_2.assign_exit_time()

        self.attendances.append(attendance_1)
        self.attendances.append(attendance_2)

    def add(self, attendance: Attendance):
        pass

    def find(self, student: Student):
        """Find a student with base in Identity Number and Role is_today."""
        for attendance in self.attendances:
            if self._is_valid(student, attendance):
                return attendance
        return

    @staticmethod
    def _is_valid(student: Student, attendance: Attendance):
        identity = student.identity_number
        return attendance.identify(identity) and attendance.is_today()


