import networkx as nx
import matplotlib.pyplot as plt
from nodes import Coach, Student

def create_graph(coaches):
	G = nx.Graph()
	for coach in coaches:
		G.add_node(coach, color='blue')
		for student in coach.students:
			G.add_node(student, color='red')
			G.add_edge(coach, student, color='green')
	nx.draw(G)
	plt.show()


c = Coach()
coaches = [c]
for i in range(10):
	s = c.add_coach()
	coaches.append(s)
	for j in range(10):
		s.add_student()
create_graph(coaches)