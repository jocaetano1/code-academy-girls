from domain.attendance_repository import AttendanceRepository
from use_cases.auth.identity_number import Authentication
from domain.attendance import Attendance
from domain.student import Student


class PointRecord:
    def __init__(self, authentication: Authentication, repository: AttendanceRepository):
        self.authentication = authentication
        self.repository = repository

    def execute(self, identity: str):
        student: Student = self.authentication.autenticate(identity)
        attendance_registred: Attendance = self.repository.find(student)
        if attendance_registred:
            return self._assign_exit(attendance_registred)
        return self._assign_entry(student)

    def _assign_entry(self, student: Student):
        attendance = Attendance.compose(student)
        attendance.assign_entry_time()
        self.repository.add(attendance)
        return attendance

    @staticmethod
    def _assign_exit(attendance_registred: Attendance):
        attendance_registred.assign_exit_time()
        return attendance_registred
