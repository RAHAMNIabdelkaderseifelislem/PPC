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

