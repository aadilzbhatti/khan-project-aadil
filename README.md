#Infection

#Description
This is my implementation of ``total_infection`` and ``limited_infection`` for my Khan Academy Project-Based Interview. There are three files in the main "solution": ``nodes.py``, ``total_infection.py``, and ``limited_infection.py``. 

#Implementation

##``nodes.py``
``nodes.py`` contains the classes for the "nodes" in the network. The network consists of two types of nodes: a ``Coach`` node and a ``Student`` node. The ``Coach`` node has multiple ``Student`` nodes, whereas a ``Student`` node can only have a ``Coach``. The network structure is essentially a forest of rooted trees, with a ``Coach`` node as the root of each tree. This was done because I wanted to simulate a classroom structure where an instructor (a ``Coach``) has access to a set of students (a ``Student``). This is not a directed network as I wanted the ability for students to infect their teachers, and vice versa. 

One can model a school with one "principal" ``Coach`` node whose "students" are more ``Coach`` nodes, which resemble teachers. These teachers would then have their own ``Student`` nodes as well as potentially other ``Coach`` nodes. The trees in the forest disjoint so as to maintain independence between instructional facilities. This allows the developer to roll out a feature to one facility without needing to worry about rolling out to another. 

##``total_infection.py``
``total_infection.py`` contains the ``total_infection`` algorithm as specified by the project guidelines. This is simply depth-first search on a graph. Since we need to access all of the children of each node at some point, it does not matter if we use depth-first or breadth-first search. The only other part to mention is that if a user passes in an object who has a parent coach, the algorithm will call ``total_infection`` on the parent so as to infect both the parent as well as its children, including the original calling argument. 