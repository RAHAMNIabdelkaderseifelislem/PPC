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

# backtracking
def backtracking(assignment):
    if len(assignment) == len(variables):
        return assignment
    var = variables[len(assignment)]
    for value in domains:
        if consistent(assignment, var, value):
            assignment.append((var, value))
            result = backtracking(assignment)
            if result is not None:
                return result
            assignment.pop()

def consistent(assignment, var, value):
    for (v, val) in assignment:
        if (var, v) in constraints or (v, var) in constraints:
            if value == val:
                return False
    return True

# query
print (backtracking([]))

# plot the graph
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(variables)
G.add_edges_from(constraints)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.show()

