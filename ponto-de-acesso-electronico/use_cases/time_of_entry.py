from datetime import datetime

from domain.attendance_repository import AttendanceRepository
from domain.student import Student
from domain.attendance import Attendance


class TimeOfEntry:
    def __init__(self, repository: AttendanceRepository):
        self.repository = repository

    def execute(self, student: Student):
        attendance = Attendance.compose(student)
        now = datetime.now()
        attendance.assign_entry_time(now)
        self.repository.add(attendance)
        return attendance