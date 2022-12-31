"""
program that solves a csp using backtracking and plots the tree of the search
"""
import networkx as nx
import matplotlib.pyplot as plt
import sys
import os
import time
import random
import math
import numpy as np
import copy
import itertools

# variables
variables = ['A', 'B', 'C', 'D', 'E', 'F']

# domains
domains = ['red', 'blue', 'green', 'yellow', 'black', 'grey']

# constraints
constraints = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'E'),
    ('A', 'F'),
    ('B', 'A'),
    ('B', 'C'),
    ('B', 'D'),
    ('B', 'F'),
    ('C', 'A'),
    ('C', 'B'),
    ('C', 'D'),
    ('C', 'E'),
    ('D', 'B'),
    ('D', 'C'),
    ('D', 'E'),
    ('D', 'F'),
    ('E', 'A'),
    ('E', 'C'),
    ('E', 'D'),
    ('E', 'F'),
    ('F', 'A'),
    ('F', 'B'),
    ('F', 'D'),
    ('F', 'E')
]

# create the graph
G = nx.Graph()

# backtracking and add nodes to the graph
def backtracking(assignment):
    if len(assignment) == len(variables):
        return assignment
    var = variables[len(assignment)]
    for value in domains:
        if consistent(assignment, var, value):
            assignment.append((var, value))
            G.add_node(str(assignment))
            G.add_edge(str(assignment), str(assignment[:-1]))
            result = backtracking(assignment)
            if result is not None:
                return result
            assignment.pop()

# check if the assignment is consistent
def consistent(assignment, var, value):
    for (v, val) in assignment:
        if (var, v) in constraints or (v, var) in constraints:
            if value == val:
                return False
    return True

# query
print (backtracking([]))

# plot the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='w', font_size=10)
plt.show()
