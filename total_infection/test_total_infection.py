from unittest import TestCase
from total import Coach, Student, total_infection

class TestTotalInfection(TestCase):
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

	"""
	This is the main test for the program. It tests, using a list of coaches
	who each have a set of students and one with another coach as a student,
	whether or not the entire set has been infected. It does this using a depth-first
	traversal of the "forest" of coaches. 
	"""
	def test_total_infection(self):
		coaches = []
		for i in range(10):
			c = Coach()
			coaches.append(c)

		import random
		for i in range(len(coaches)):
			num_students = int(1 + random.random() * 10)
			for _ in range(num_students):
				coaches[i].add_student()

		s1 = int(1 + random.random() * 10)		# here we add a coach-coach relationship
		s2 = 10 - s1
		coaches[s1].add_coach()

		for coach in coaches:
			total_infection(coach)				# infect them all!

		"""
		Since not every coach coaches other coaches (wow), we need to loop 
		through all of the coaches to look at their children. Essentially
		right now we have a forest which consists of coaches at the roots, 
		where a child may be a coach or a student. So we do a depth-first
		traversal of each tree in the forest.
		"""	
		for coach in coaches:
			self.assertTrue(coach.infected)
			s = [coach]
			while s:
				v = s.pop()
				self.assertTrue(v.infected)
				if isinstance(v, Coach):
					for student in v.students:
						s.append(student)