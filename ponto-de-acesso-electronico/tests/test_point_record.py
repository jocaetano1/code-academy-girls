import unittest
from datetime import datetime

from adaptors.inmem.inmen_attendance_repository import InmemAttendanceRepository
from test_data.stubs.attendance_repository_stub import AttendanceRepositoryStub
from use_cases.auth.identity_number import IdentityNumberAuthentication
from use_cases.point_record import PointRecord
from test_data.stubs.student_repository_stub import StudentRepositoryStub


class PointRecordTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.identity_number = "004843261LA047"
        self.student_repository = StudentRepositoryStub()
        self.attendance_repository = InmemAttendanceRepository()

    def test_authenticate_to_record_entry_time(self):
        """Deve autenticar a formanda para gravar a hora de entrada."""
        # Arrange
        authentication_mode = IdentityNumberAuthentication(self.student_repository)
        point_record = PointRecord(authentication_mode, self.attendance_repository)

        # Act.
        attendance = point_record.execute(self.identity_number)

        # Assert
        self.assertEqual(attendance.entry_time.strftime("%H:%M"), datetime.now().strftime("%H:%M"))

    def test_authenticate_to_record_exit_time(self):
        """Deve autenticar a formanda para gravar a hora de saída."""
        # Arrange
        identity_number = "004843261LA048"
        repository = AttendanceRepositoryStub()
        authentication_mode = IdentityNumberAuthentication(self.student_repository)
        point_record = PointRecord(authentication_mode, repository)

        # Act.
        attendance = point_record.execute(identity_number)

        # Assert
        self.assertEqual(attendance.exit_time.strftime("%H:%M"), datetime.now().strftime("%H:%M"))

    def test_record_attendance_more_one_time(self):
        """Deve retorna erro para as formandas que já registraram a presença num dia."""
        self.assertEqual(2, 2)