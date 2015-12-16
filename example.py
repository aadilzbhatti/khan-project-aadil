from nodes import *
from limited_infection import *
from total_infection import *
from visual import *

"""
This file is used to display examples of using the infection algorithms
as well as the visualization. In this example, we will construct several
schools with a "principal" head coach with several "teacher" coaches, each
with several students as children. We will then infect them using total_infection, 
visualize, then infect them using limited_infection and visualize.
"""
heads = []
for i in range(4):
	p = Coach()
	heads.append(p)
	for j in range(3):
		t = p.add_coach()
		for k in range(3):
			t.add_student()

"""
We have now created a set of 4 schools, each with 1 principal, 3 teachers, 
and 3 students per teacher. We need to keep it small due to the limitations
of the size of matplotlib's figures. 
"""

# 1st visualization: no infection (see no_infection.png)
graph(heads)

# Now we do a total infection
for head in heads:
	total_infection(head)

# 2nd visualization: total infection (see total_infection.png)
graph(heads)

# One can see that everyone has been infected. 

# Now we do a limited infection
# For this we need to restablish the schools because the original schools are infected
heads = []
for i in range(4):
	p = Coach()
	heads.append(p)
	for j in range(3):
		t = p.add_coach()
		for k in range(3):
			t.add_student()

# The actual size is 36 here, so we go under to show the limited infection
limit = 32

# We can see how many coaches we can infect. In this case, 2.
print(infectable(heads, 32))

# Now we infect
for head in heads:
	limit = limited_infection(head, limit)

# 3rd visualization: limited infection (see limited_infection.png)
graph(heads)

# One can see that only two of the four schools have been infected. 