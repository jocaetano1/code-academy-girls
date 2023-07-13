import abc

from domain.attendance import Attendance


class AttendanceRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, attendance: Attendance):
        """Add new attendance of student."""
        pass
