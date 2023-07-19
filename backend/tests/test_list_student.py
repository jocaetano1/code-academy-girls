import unittest

from adaptors.inmem.inmem_student_repository import InmemStudentRepository
from use_cases.list_student import ListStudent


class ListStudentTestCase(unittest.TestCase):
    def test_list_student(self):
        repository = InmemStudentRepository()
        list_student = ListStudent(repository)
        students = list_student.execute()
        self.assertGreaterEqual(len(students), 0)
