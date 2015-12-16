from unittest import TestCase
from nodes import Coach, Student

class TestNodes(TestCase):
	def setUp(self):
		self.coach = Coach()
		for i in range(10):
			self.coach.add_student()

	def test_add_student(self):
		num_students = len(self.coach.students)
		self.coach.add_student()
		self.assertTrue(num_students != len(self.coach.students))

	def test_add_coach(self):
		c1 = Coach()
		c2 = Coach()
		c1.add_coach(c2)
		c1.add_coach()
		self.assertEqual(len(c1.students), 2)
		self.assertEqual(c2.coach, c1)

	def test_student_coach(self):
		for student in self.coach.students:
			self.assertEqual(student.coach, self.coach)

	def test_infected_coach(self):
		c = Coach()
		c.infect()
		self.assertTrue(c.infected)

	def test_infected_student(self):
		s = Student()
		s.infect()
		self.assertTrue(s.infected)

	def test_count(self):
		self.assertEqual(self.coach.count(), 12)

if __name__ == '__main__':
    unittest.main()