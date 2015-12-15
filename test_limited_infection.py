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
	The more realistic case where we are seeing how many coaches
	in a set of coaches can be infected
	"""
	def test_limited_infection_on_forest(self):
		coaches = []
		for i in range(10):									# create a forest of 10 trees
			c = Coach()
			coaches.append(c)
			import random
			num = int(1 + random.random() * 10)
			for j in range(num):							# add between 1 and 10 child coaches
				c1 = c.add_coach()
				students = int(1 + random.random() * 10)
				for _ in range(students):					# add between 1 and 10 students
					c1.add_student()

		abs_limit = 0
		for coach in coaches:
			abs_limit += coach.count()						# abs_limit should be a number in the hundreds now
		
		limit = abs_limit									# to show that we can give everyone the new feature
		for coach in coaches:
			limit = limited_infection(coach, limit)
		self.assertEqual(limit, 0)

		limit = abs_limit - coaches[-1].count()				# to show that we can't give everyone the new feature
		for i in range(len(coaches) - 1):
			limit = limited_infection(coaches[i], limit)
		self.assertFalse(limited_infection(coaches[-1], limit))

		limit = abs_limit - coaches[-1].count()				# a way of showing how many coaches we can infect with this limit
		self.assertEqual(infectable(coaches, limit), 8)