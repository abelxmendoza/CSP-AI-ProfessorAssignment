from constraint import Problem, AllDifferentConstraint

# Create a CSP problem instance
problem = Problem()

# Define variables
professors = ['A_CPSC101', 'A_CPSC103', 'B_CPSC101', 'B_CPSC102', 'B_CPSC104', 'C_CPSC102', 'C_CPSC103']
courses = ['CPSC101', 'CPSC102', 'CPSC103', 'CPSC104']

# Define domains
for prof in professors:
    problem.addVariable(prof, courses)

# Define unary constraints
problem.addConstraint(lambda A_CPSC103: A_CPSC103 != 'CPSC103', ('A_CPSC103',))

# Define binary constraints
problem.addConstraint(AllDifferentConstraint(), ('A_CPSC101', 'A_CPSC103', 'B_CPSC101', 'B_CPSC102', 'B_CPSC104', 'C_CPSC102', 'C_CPSC103'))
problem.addConstraint(lambda A_CPSC101, B_CPSC101, B_CPSC104: A_CPSC101 == B_CPSC101 == B_CPSC104, ('A_CPSC101', 'B_CPSC101', 'B_CPSC104'))
problem.addConstraint(lambda B_CPSC102, C_CPSC102, C_CPSC103: B_CPSC102 == C_CPSC102 == C_CPSC103, ('B_CPSC102', 'C_CPSC102', 'C_CPSC103'))

# Find a solution
solution = problem.getSolution()

# Display the solution if found
if solution:
    print("Solution:")
    for variable, value in solution.items():
        print(f"{variable}: {value}")
else:
    print("No solution found.")
