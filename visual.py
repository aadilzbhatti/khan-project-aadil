import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from nodes import Coach, Student
from limited_infection import limited_infection

def graph(coaches):
	G = nx.Graph()
	for coach in coaches:
		s = [coach]
		current = coach
		while s:
			v = s.pop()
			G.add_edge(current, v)
			if isinstance(v, Coach):
				for student in v.students:
					s.append(student)
					current = v
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
	pos = nx.spring_layout(G)
	nx.draw_networkx_nodes(G, pos=pos, node_color=node_colors, node_size=50)
	nx.draw_networkx_edges(G, pos=pos)
	orange_patch = mpatches.Patch(color='orange', label='Uninfected Coach')
	red_patch = mpatches.Patch(color='red', label='Uninfected Student')
	green_patch = mpatches.Patch(color='green', label='Infected Coach')
	blue_patch = mpatches.Patch(color='blue', label='Infected Student')
	plt.legend(handles=[orange_patch, red_patch, green_patch, blue_patch], loc=0, prop={'size': 6})
	plt.show()