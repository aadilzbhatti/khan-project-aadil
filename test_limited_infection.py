from unittest import TestCase
from nodes import Coach, Student
from limited_infection import limited_infection, infectable

class TestLimitedInfection(TestCase):
	"""
	Constructing a basic tree with a "principal" coach 
	at the root, 10 "teacher" coaches and 10 students 
	for each "teacher" coach
	"""
	def setUp(self):
		self.head = Coach()
		for i in range(10):
			c = self.head.add_coach()
			for j in range(10):
				c.add_student()

	"""
	The basic limited_infection case, where we are seeing
	if one coach can be infected or not.
	"""
	def test_single_limited_infection(self):
		self.assertFalse(limited_infection(self.head, 99))
		self.assertEqual(limited_infection(self.head, 100), 0)

	"""
	The more realistic cases where we are seeing how many coaches
	in a set of coaches can be infected. This test uses a full limit
	to ensure everyone gets infected. 
	"""
	def test_forest_with_full_limit(self):
		coaches = []
		# create a forest of 10 trees
		for i in range(10):									
			c = Coach()
			coaches.append(c)
			import random
			num = int(1 + random.random() * 10)
			# add between 1 and 10 child coaches
			for j in range(num):							
				c1 = c.add_coach()
				students = int(1 + random.random() * 10)
				# add between 1 and 10 students
				for _ in range(students):					
					c1.add_student()

		abs_limit = 0
		for coach in coaches:
			abs_limit += coach.count()	

		# abs_limit should be a number in the hundreds now					
		limit = abs_limit									
		for coach in coaches:
			limit = limited_infection(coach, limit)

		# to show that we can give everyone the new feature
		self.assertEqual(limit, 0)

	"""
	Tests a less than full limit on a forest to ensure that not 
	everyone gets infected. 
	"""
	def test_forest_with_less_limit(self):
		coaches = []
		# create a forest of 10 trees
		for i in range(10):									
			c = Coach()
			coaches.append(c)
			import random
			num = int(1 + random.random() * 10)
			# add between 1 and 10 child coaches
			for j in range(num):							
				c1 = c.add_coach()
				students = int(1 + random.random() * 10)
				# add between 1 and 10 students
				for _ in range(students):					
					c1.add_student()

		abs_limit = 0
		for coach in coaches:
			abs_limit += coach.count()

		limit = abs_limit - coaches[-1].count()				
		for i in range(len(coaches) - 1):
			limit = limited_infection(coaches[i], limit)

		# to show that we can't give everyone the new feature
		self.assertFalse(limited_infection(coaches[-1], limit))

	"""
	These test whether we can infect the entire tree from 
	a child node.
	"""
	def test_limited_infection_from_student_to_parent(self):
		c = Coach()
		for i in range(5):
			c.add_student()
		s = c.students[0]
		f = limited_infection(s, 3)
		self.assertFalse(f)

	def test_limited_infection_from_coach_to_parent(self):
		c = Coach()
		for i in range(5):
			c1 = c.add_coach()
			for j in range(5):
				c1.add_student()
		coach = c.students[0]
		f = limited_infection(coach, 20)
		self.assertFalse(f)

	"""
	Tests if a coach has been infected, do not re-infect.
	"""
	def test_limited_infection_when_already_infected(self):
		c = Coach()
		for i in range(5):
			c.add_student()
		limit = limited_infection(c, 8)
		self.assertEqual(limit, 2)
		limit = limited_infection(c, 8)
		self.assertEqual(limit, 8)

	"""
	Test to see how many coaches we can infect with the 
	given limit.
	"""
	def test_infectable(self):
		c = Coach()
		coaches = [c]
		for i in range(5):
			c1 = c.add_coach()
			coaches.append(c1)
			for j in range(5):
				c1.add_student()
		limit = 0
		for i in range(len(coaches) - 1):
			limit += coaches[i].count()
		self.assertEqual(infectable(coaches, limit), 5)