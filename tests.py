import unittest
from student import Student

class StudentTest(unittest.TestCase):
    student = Student()
    def test_check_marks_1(self):
        self.assertEqual(self.student.check_marks(85), 'B', "Wrong evaluation, it should be 'B'")
    def test_check_marks_2(self):
        self.assertEqual(self.student.check_marks(75), 'C', "Wrong evaluation, it should be 'C'")