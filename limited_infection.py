from nodes import Coach, Student

"""
The implementation of limited_infection. Essentially,
we pass in a root coach and a limit. If there are more
nodes than the limit, then we can't infect this node as
some nodes would end up not infected. In this case, we
return False to signify that this node is unable to infect. 
In the better case, we do a depth-first traversal and infect
every child in the tree if the limit is large enough. We then
return the new limit for further use.
"""
def limited_infection(coach, limit):
	if isinstance(coach, Student) or coach.coach is not None:
		return limited_infection(coach.coach, limit)
	if coach.count_infected() == coach.count():
		return limit
	if coach.count() > limit:
		return False
	s = [coach]
	while s:
		v = s.pop()
		v.infect()
		if isinstance(v, Coach):
			for student in v.students:
				s.append(student)
	return limit - coach.count()

"""
This method determines how many coaches in a set of coaches
can be infected within a certain limit. 
"""
def infectable(coaches, limit):
	for i in range(len(coaches)):
		limit -= coaches[i].count()
		if limit < 0:
			return i
	return len(coaches)