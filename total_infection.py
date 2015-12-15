from nodes import Coach

"""
The total infection algorithm. Infects entire classroom in a 
depth-first traversal of the class. If the original argument
has a coach, then we recursively infect the parent coach so 
as to infect both the current coach (and potential students)
as well as the parent coach's students.
"""
def total_infection(coach):
	if isinstance(coach, Student) or coach.coach is not None:
		total_infection(coach.coach)
	coach.infect()
	s = [coach]
	while s:
		v = s.pop()
		v.infect()
		if isinstance(v, Coach):
			for student in v.students:
				s.append(student)