import unittest
from datetime import datetime

from adaptors.inmem.inmen_attendance_repository import InmemAttendanceRepository
from use_cases.authentication import IdentityNumberAuth
from use_cases.time_of_entry import TimeOfEntry
from test_data.stubs.student_repository_stub import StudentRepositoryStub


class TimeOfEntryTestCase(unittest.TestCase):

    def test_record_entry_time(self):
        """Deve registrar a hora de entrada da aluna."""
        # Arrange
        identity_number = "004843261LA047"
        student_repository = StudentRepositoryStub()
        auth = IdentityNumberAuth(student_repository)
        student = auth.autenticate(identity_number)

        # Act.
        repository = InmemAttendanceRepository()
        time_of_entry = TimeOfEntry(repository)
        attendance = time_of_entry.execute(student)

        # Assert
        self.assertEqual(attendance.entry_time.strftime("%H:%M"), datetime.now().strftime("%H:%M"))
        self.assertEqual(attendance.created, datetime.now().date())
