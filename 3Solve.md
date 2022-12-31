# Solve CSP Algorithms

## Generate-and-test

is a brute-force algorithm that enumerates all possible assignments to the variables and checks whether each assignment satisfies the constraints. This algorithm is not efficient for large problems.

### Example

The following is a CSP that represents the map coloring problem. The variables are the states, the domains are the colors, and the constraints are the restrictions that no two adjacent states can have the same color.

* variables: WA, NT, SA, Q, NSW, V, T
* domains: red, green, blue
* constraints: 
    - WA != NT, 
    - WA != SA, 
    - NT != SA, 
    - NT != Q, 
    - SA != Q, 
    - SA != NSW, 
    - SA != V, 
    - Q != NSW, 
    - NSW != V

```prolog
% map coloring problem
% variables: WA, NT, SA, Q, NSW, V, T
% domains: red, green, blue
% constraints: 
%     - WA != NT, 
%     - WA != SA, 
%     - NT != SA, 
%     - NT != Q, 
%     - SA != Q, 
%     - SA != NSW, 
%     - SA != V, 
%     - Q != NSW, 
%     - NSW != V

% variables
variable(WA).
variable(NT).
variable(SA).
variable(Q).
variable(NSW).
variable(V).
variable(T).

% domains
domain(red).
domain(green).
domain(blue).

% constraints
constraint(WA, NT).
constraint(WA, SA).
constraint(NT, SA).
constraint(NT, Q).
constraint(SA, Q).
constraint(SA, NSW).
constraint(SA, V).
constraint(Q, NSW).
constraint(NSW, V).

% generate-and-test
generate_and_test(Variables) :-
    generate(Variables),
    test(Variables).

generate([]).
generate([Variable|Variables]) :-
    domain(Variable),
    generate(Variables).

test([]).
test([Variable|Variables]) :-
    \+ (member(V, Variables), constraint(Variable, V)),
    test(Variables).

% query
?- generate_and_test([WA, NT, SA, Q, NSW, V, T]).
```

result:

```prolog
WA = red,
NT = green,
SA = blue,
Q = red,
NSW = green,
V = red,
T = blue ;
WA = red,
NT = green,
SA = blue,
Q = red,
NSW = green,
V = blue,
T = red ;
WA = red,
NT = green,
SA = blue,
Q = red,
NSW = blue,
V = red,
T = green ;
WA = red,
NT = green,
SA = blue,
Q = red,
NSW = blue,
V = green,
T = red ;
WA = red,
NT = green,
SA = blue,
Q = green,
NSW = red,
V = blue,
T = red ;
WA = red,
NT = green,
SA = blue,
Q = green,
NSW = blue,
V = red,
T = red ;
WA = red,
NT = green,
SA = blue,
Q = blue,
NSW = red,
V = green,
T = red ;
WA = red,
NT = green,
SA = blue,
Q = blue,
NSW = green,
V = red,
T = red ;
......
```

## Backtracking

is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons each partial candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

### Example

The following is a CSP that represents the map coloring problem. The variables are the states, the domains are the colors, and the constraints are the restrictions that no two adjacent states can have the same color.

* variables: WA, NT, SA, Q, NSW, V, T
* domains: red, green, blue
* constraints: 
    - WA != NT, 
    - WA != SA, 
    - NT != SA, 
    - NT != Q, 
    - SA != Q, 
    - SA != NSW, 
    - SA != V, 
    - Q != NSW, 
    - NSW != V

```python
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
        if consistent(assignment, (var, value)):
            assignment.append((var, value))
            result = backtracking(assignment)
            if result is not None:
                return result
            assignment.pop()

def consistent(assignment, (var, value)):
    for (v, val) in assignment:
        if (var, v) in constraints or (v, var) in constraints:
            if value == val:
                return False
    return True

# query
print backtracking([])
```

result:

```python
[('WA', 'red'), ('NT', 'green'), ('SA', 'blue'), ('Q', 'red'), ('NSW', 'green'), ('V', 'red'), ('T', 'red')]
```

## k-consistency

is a property of a constraint satisfaction problem that is satisfied by a solution if and only if the solution is consistent with at least k of the constraints.

for specific number of K we define the following Algorithms:

* k = 1 : node consistency
* k = 2 : arc consistency
* k = 3 : path consistency
* k > 3 : k-consistency

### node consistency

is a property of a constraint satisfaction problem that is satisfied by a solution if and only if the solution is consistent with at least one of the constraints.

### arc consistency

is a property of a constraint satisfaction problem that is satisfied by a solution if and only if the solution is consistent with at least two of the constraints.

### path consistency

is a property of a constraint satisfaction problem that is satisfied by a solution if and only if the solution is consistent with at least three of the constraints.

### k-consistency

is a property of a constraint satisfaction problem that is satisfied by a solution if and only if the solution is consistent with at least k of the constraints.

### Implementation

```python
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
        if consistent(assignment, (var, value), k):
            assignment.append((var, value))
            result = k_consistency(assignment, k)
            if result is not None:
                return result
            assignment.pop()

def consistent(assignment, (var, value), k):
    c = 0
    for (v, val) in assignment:
        if (var, v) in constraints or (v, var) in constraints:
            if value == val:
                c += 1
                if c >= k:
                    return False
    return True

# query
print k_consistency([], 1)
print k_consistency([], 2)
print k_consistency([], 3)
```

result:

```python
[('WA', 'red'), ('NT', 'green'), ('SA', 'blue'), ('Q', 'red'), ('NSW', 'green'), ('V', 'red'), ('T', 'red')]
[('WA', 'red'), ('NT', 'red'), ('SA', 'green'), ('Q', 'red'), ('NSW', 'red'), ('V', 'red'), ('T', 'red')]
[('WA', 'red'), ('NT', 'red'), ('SA', 'red'), ('Q', 'red'), ('NSW', 'red'), ('V', 'red'), ('T', 'red')]
```

## Bound Consistency

is a property of a constraint satisfaction problem that is satisfied by a solution if and only if the solution is consistent with at least one of the constraints.

### Implementation

```python
# bound consistency
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

# bound consistency
def bound_consistency(assignment):
    if len(assignment) == len(variables):
        return assignment
    var = variables[len(assignment)]
    for value in domains:
        if consistent(assignment, (var, value)):
            assignment.append((var, value))
            result = bound_consistency(assignment)
            if result is not None:
                return result
            assignment.pop()

def consistent(assignment, (var, value)):
    for (v, val) in assignment:
        if (var, v) in constraints or (v, var) in constraints:
            if value == val:
                return False
    return True

# query
print bound_consistency([])
```

result:

```python
[('WA', 'red'), ('NT', 'green'), ('SA', 'blue'), ('Q', 'red'), ('NSW', 'green'), ('V', 'red'), ('T', 'red')]
```
