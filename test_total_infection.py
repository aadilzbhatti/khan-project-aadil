from unittest import TestCase
from nodes import Coach, Student
from total_infection import total_infection

class TestTotalInfection(TestCase):
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

		s1 = int(random.random() * 10)		# here we add a coach-coach relationship
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

if __name__ == '__main__':
    unittest.main()