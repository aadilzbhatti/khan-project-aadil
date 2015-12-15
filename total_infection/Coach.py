class Coach:
	next_id = 0
	def __init__(self):
		self.students = []
		self.infected = False
		self.id_ = Coach.next_id
		Coach.next_id += 1
		self.coach = None

	def __str__(self):
		ret = "Coach " + str(self.id_) + "\nStudents: ["
		for student in self.students:
			ret += str(student) + " "
		ret += "]"
		return ret

	def infect(self):
		self.infected = True

	def add_student(self):
		s = Student()
		self.students.append(s)
		s.coach = self

	def add_coach(self, coach=None):
		c = coach if coach else Coach()
		self.students.append(c)
		c.coach = self

class Student:
	next_id = 0
	def __init__(self, id_='', coach=None):
		self.coach = coach
		self.infected = False
		self.id_ = Student.next_id
		Student.next_id += 1

	def __str__(self):
		return "Student " + str(self.id_)

	def infect(self):
		self.infected = True

def total_infection(coach):
	if isinstance(coach, Student):
		print("HEY!")