import abc

from domain.attendance import Attendance
from domain.student import Student


class AttendanceRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, attendance: Attendance):
        """Add new attendance of student."""
        pass

    @abc.abstractmethod
    def find(self, student: Student):
        """Find attendance of student."""
        pass
