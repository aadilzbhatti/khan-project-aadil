#Infection

#Description
This is my implementation of ``total_infection`` and ``limited_infection`` for my Khan Academy Project-Based Interview. There are three files in the main "solution": ``nodes.py``, ``total_infection.py``, and ``limited_infection.py``. 

#Problem Statement
The problem I am trying to solve is the problem of rolling out a new feature of a piece of software. We can either introduce the feature to everyone all at once or release it over time to smaller groups of people. We can solve this problem by using "infections". A "total infection" is "infecting" the entire population which we are servicing, whereas a "limited infection" is "infecting" the population selectively. I have implemented algorithms to model "total infection" and "limited infection" in the files described below. 

#Implementation

##``nodes.py``
``nodes.py`` contains the classes for the "nodes" in the network. The network consists of two types of nodes: a ``Coach`` node and a ``Student`` node. The ``Coach`` node has multiple ``Student`` nodes, whereas a ``Student`` node can only have a ``Coach``. The network structure is essentially a forest of rooted trees, with a ``Coach`` node as the root of each tree. This was done because I wanted to simulate a classroom structure where an instructor (a ``Coach``) has access to a set of students (a ``Student``). This is not a directed network as I wanted the ability for students to infect their teachers, and vice versa. 

One can model a school with one "principal" ``Coach`` node whose "students" are more ``Coach`` nodes, which resemble teachers. These teachers would then have their own ``Student`` nodes as well as potentially other ``Coach`` nodes. The trees in the forest are disjoint so as to maintain independence between instructional facilities. This allows the developer to roll out a feature to one facility without needing to worry about rolling out to another. 

##``total_infection.py``
``total_infection.py`` contains the ``total_infection`` algorithm as specified by the project guidelines. This is simply depth-first search on a graph. Since we need to access all of the children of each node at some point, it does not matter if we use depth-first or breadth-first search. The only other part to mention is that if a user passes in an object who has a parent coach, the algorithm will call ``total_infection`` on the parent so as to infect both the parent as well as its children, including the original calling argument. 

##``limited_infection.py``
``limited_infection.py`` contains the ``limited_infection`` algorithm as specified by the project guidelines. This is slightly more involved than ``total_infection`` as we need to consider the number of people we want to infect. We essentially want to infect `n` individuals, however, we do not want to infect a coach without being able to infect the coach's students. Then we cannot infect a coach tree without the total number of nodes in that tree being less than or equal to the limit `n`. We do this by invoking a ``count`` function that counts how many children nodes a certain coach has. If this value is greater than the allowed limit, we do not infect the coach or its children. Otherwise, we infect all of the nodes in the tree. This algorithm is designed to operate on a single coach-student tree, however, it is more useful when we have a forest because then we can see how many coaches we can infect out of a set of coaches. 

# Visualization
I added the ability for a user to see exactly how they are infecting the population. To see this, construct your coaches/students as you see fit. Then you simply import ``visual`` and run the ``graph`` method on the set of coaches. You will need to pass a list as a parameter as it constructs the visualization as a forest. The ``graph`` method uses the ``networkx`` to construct a forest of undirected graphs, one graph per coach. The nodes are color-coded to ensure clarity. To see the visualization, you will need ``matplotlib`` and ``networkx`` installed. You can simply run ``pip install <module>`` to get them. 

If you run ``total_infection`` or ``limited_infection`` on your set of coaches, you can then graph the set to see the results. 

# Examples
I have included a file called ``example.py`` to show how to use the methods outlined above. If you have any questions, please let me know. 