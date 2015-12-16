import networkx as nx
import matplotlib.pyplot as plt
from nodes import Coach, Student
from limited_infection import limited_infection

def graph(coaches):
	G = nx.Graph()
	for coach in coaches:
		for student in coach.students:
			G.add_edge(coach, student)
	pos = nx.spring_layout(G)
	node_colors = []
	for n in G.nodes():
		if isinstance(n, Student):
			if n.infected:
				node_colors.append("blue")
			else:
				node_colors.append("red")
		else:
			if n.infected:
				node_colors.append("green")
			else:
				node_colors.append("orange")
	nx.draw_networkx_nodes(G, pos=pos, node_color=node_colors)
	nx.draw_networkx_edges(G, pos=pos)
	plt.legend(["Coaches"], loc=0)
	plt.show()


c = Coach()
coaches = [c]
for i in range(5):
	s = c.add_coach()
	coaches.append(s)
	for j in range(5):
		s.add_student()
for i in range(5):
	c1 = Coach()
	coaches.append(c1)
	for j in range(5):
		c1.add_student()

for coach in coaches:
	limit = limited_infection(coach, 20)
graph(coaches)