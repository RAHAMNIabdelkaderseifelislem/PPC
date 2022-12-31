from constraint import *

problem = Problem()

problem.addVariables(["WA", "NT", "SA", "Q", "NSW", "V", "T"], ["red", "green", "blue"])

problem.addConstraint(AllDifferentConstraint(), ["WA", "NT", "SA", "Q", "NSW", "V", "T"])

solutions = problem.getSolutions()

print(solutions)
