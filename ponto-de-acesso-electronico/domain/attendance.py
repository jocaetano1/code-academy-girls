from datetime import datetime, date
from dataclasses import dataclass

from domain.student import Student


@dataclass(init=False)
class Attendance:
    student: Student
    entry_time: datetime
    exit_time: datetime
    created: date

    @staticmethod
    def compose(student: Student):
        attendance = Attendance()
        attendance.student = student
        attendance.created = datetime.now().date()
        return attendance

    def assign_entry_time(self, entry_time: datetime):
        self.entry_time = entry_time

    def assign_exit_time(self, exit_time: datetime):
        self.exit_time = exit_time
