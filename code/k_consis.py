# k-consistency
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

# k-consistency
def k_consistency(assignment, k):
    if len(assignment) == len(variables):
        return assignment
    var = variables[len(assignment)]
    for value in domains:
        if consistent(assignment, var, value, k):
            assignment.append((var, value))
            result = k_consistency(assignment, k)
            if result is not None:
                return result
            assignment.pop()

def consistent(assignment, var, value, k):
    c = 0
    for (v, val) in assignment:
        if (var, v) in constraints or (v, var) in constraints:
            if value == val:
                c += 1
                if c >= k:
                    return False
    return True

# query
print(k_consistency([], 1))
print(k_consistency([], 2))
print(k_consistency([], 3))