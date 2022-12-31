# map coloring problem
# variables: WA, NT, SA, Q, NSW, V, T
# domains: red, green, blue
# constraints:
#     - WA != NT,
#     - WA != SA,
#     - NT != SA,
#     - NT != Q,
#     - SA != Q,
#     - SA != NSW,
#     - SA != V,
#     - Q != NSW,
#     - NSW != V

# variables
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# domains
domains = ['red', 'green', 'blue']

# constraints
constraints = [
    ('WA', 'NT'),
    ('WA', 'SA'),
    ('NT', 'SA'),
    ('NT', 'Q'),
    ('SA', 'Q'),
    ('SA', 'NSW'),
    ('SA', 'V'),
    ('Q', 'NSW'),
    ('NSW', 'V')
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
print(backtracking([]))