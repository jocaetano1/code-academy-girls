from domain.attendance_repository import AttendanceRepository
from domain.attendance import Attendance


class InmemAttendanceRepository(AttendanceRepository):
    attendances: list = []

    def add(self, attendance: Attendance):
        self.attendances.append(attendance)
