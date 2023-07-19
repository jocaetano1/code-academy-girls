from datetime import datetime, date, time
from dataclasses import dataclass

from domain.student import Student


@dataclass(init=False)
class Attendance:
    student: Student
    entry_time: time
    exit_time: time
    created: date

    @staticmethod
    def compose(student: Student):
        attendance = Attendance()
        attendance.student = student
        attendance.created = datetime.now().date()
        return attendance

    def assign_entry_time(self):
        entry_time = datetime.now().time()
        self.entry_time = entry_time

    def assign_exit_time(self):
        exit_time = datetime.now().time()
        self.exit_time = exit_time

    def identify(self, identity: str):
        return self.student.identity_number == identity

    def is_today(self):
        today = datetime.now().date().today()
        return self.created.today() == today
