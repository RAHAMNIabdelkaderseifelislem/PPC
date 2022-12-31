# Init to Prolog

## Description

the prolog programming language is a logic programming language. It is a general purpose programming language, but it is especially useful for artificial intelligence and constraint programming.

## define a predicate

```prolog
% define a predicate
% predicate name: father
% predicate arguments: X, Y
father(X, Y) :- X is the father of Y.
```

## define a fact

```prolog
% define a fact
% fact name: father
% fact arguments: X, Y
father(X, Y).
```

## define a full CSP

our CSP is :
* variables: nodes (A,B,C,D,E,F)
* domains: colours {red, blue, green, yellow, black, grey}
* constraints:
    * Color A different from B, C, E, F
    * Color B different from A, C, D, F
    * Color C different from A, B, D, E
    * Color D different from B, C, E, F
    * Color E different from A, C, D, F
    * Color F different from A, B, D, E

### 1. in swi-prolog with the use of the library clpfd

```prolog
% load the library clpfd
:- use_module(library(clpfd)).

% define the variables
colours([red, blue, green, yellow, black, grey]).
variables([A,B,C,D,E,F]).
variables_domains([], []).
variables_domains([V|Vs], [D|Ds]) :-
    colours(Ds),
    variables_domains(Vs, Ds).

% define the constraints

% Color A different from B, C, E, F
constraint1(A, B, C, E, F) :-
    A #\= B,
    A #\= C,
    A #\= E,
    A #\= F.

% Color B different from A, C, D, F
constraint2(A, B, C, D, F) :-
    B #\= A,
    B #\= C,
    B #\= D,
    B #\= F.

% Color C different from A, B, D, E
constraint3(A, B, C, D, E) :-
    C #\= A,
    C #\= B,
    C #\= D,
    C #\= E.

% Color D different from B, C, E, F
constraint4(B, C, D, E, F) :-
    D #\= B,
    D #\= C,
    D #\= E,
    D #\= F.

% Color E different from A, C, D, F
constraint5(A, C, D, E, F) :-
    E #\= A,
    E #\= C,
    E #\= D,
    E #\= F.

% Color F different from A, B, D, E
constraint6(A, B, D, E, F) :-
    F #\= A,
    F #\= B,
    F #\= D,
    F #\= E.

% define the CSP
csp(A, B, C, D, E, F) :-
    variables([A,B,C,D,E,F]),
    variables_domains([A,B,C,D,E,F], [D1,D2,D3,D4,D5,D6]),
    constraint1(A, B, C, E, F),
    constraint2(A, B, C, D, F),
    constraint3(A, B, C, D, E),
    constraint4(B, C, D, E, F),
    constraint5(A, C, D, E, F),
    constraint6(A, B, D, E, F).

% solve the CSP
solve_csp(A, B, C, D, E, F) :-
    csp(A, B, C, D, E, F),
    labeling([], [A,B,C,D,E,F]).
```

### 2. in gnuprolog

```prolog
% define the variables
colours([red, blue, green, yellow, black, grey]).
variables([A,B,C,D,E,F]).
variables_domains([], []).
variables_domains([V|Vs], [D|Ds]) :-
    colours(Ds),
    variables_domains(Vs, Ds).

% define the constraints

% Color A different from B, C, E, F
constraint1(A, B, C, E, F) :-
    A \= B,
    A \= C,
    A \= E,
    A \= F.

% Color B different from A, C, D, F
constraint2(A, B, C, D, F) :-
    B \= A,
    B \= C,
    B \= D,
    B \= F.

% Color C different from A, B, D, E
constraint3(A, B, C, D, E) :-
    C \= A,
    C \= B,
    C \= D,
    C \= E.

% Color D different from B, C, E, F
constraint4(B, C, D, E, F) :-
    D \= B,
    D \= C,
    D \= E,
    D \= F.

% Color E different from A, C, D, F
constraint5(A, C, D, E, F) :-
    E \= A,
    E \= C,
    E \= D,
    E \= F.

% Color F different from A, B, D, E
constraint6(A, B, D, E, F) :-
    F \= A,
    F \= B,
    F \= D,
    F \= E.

% define the CSP
csp(A, B, C, D, E, F) :-
    variables([A,B,C,D,E,F]),
    variables_domains([A,B,C,D,E,F], [D1,D2,D3,D4,D5,D6]),
    constraint1(A, B, C, E, F),
    constraint2(A, B, C, D, F),
    constraint3(A, B, C, D, E),
    constraint4(B, C, D, E, F),
    constraint5(A, C, D, E, F),
    constraint6(A, B, D, E, F).

% solve the CSP
solve_csp(A, B, C, D, E, F) :-
    csp(A, B, C, D, E, F),
    labeling([], [A,B,C,D,E,F]).
```
