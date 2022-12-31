# CSP

Constraint Satisfaction Problem is a model of problem solving in which the goal is to find a solution that satisfies a set of constraints. CSP is a generalization of the Boolean satisfiability problem, which is the problem of finding a truth assignment to a set of Boolean variables that satisfies a set of Boolean constraints. CSP is a generalization of the Boolean satisfiability problem, which is the problem of finding a truth assignment to a set of Boolean variables that satisfies a set of Boolean constraints.

## Representation of CSP

A CSP is defined by a set of variables, a set of domains, and a set of constraints. The variables are the entities whose values are to be determined. The domains are the possible values that the variables can take. The constraints are the restrictions on the values that the variables can take.

## Example

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
