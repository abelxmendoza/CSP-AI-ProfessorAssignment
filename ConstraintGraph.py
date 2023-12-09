import networkx as nx
import matplotlib.pyplot as plt

def add_constraints(graph, constraints):
    for constraint in constraints:
        graph.add_edge(constraint[0], constraint[1])

def draw_constraint_graph(constraints):
    graph = nx.Graph()
    add_constraints(graph, constraints)

    pos = nx.spring_layout(graph)  # Positioning of nodes
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color='lightblue', font_size=10, node_size=1000)
    plt.title("Constraint Graph")
    plt.show()

# List of binary constraints
binary_constraints = [
    ('A_CPSC101', 'A_CPSC103'),
    ('A_CPSC101', 'B_CPSC101'),
    ('A_CPSC101', 'B_CPSC102'),
    ('A_CPSC101', 'B_CPSC104'),
    ('A_CPSC101', 'C_CPSC102'),
    ('A_CPSC101', 'C_CPSC103'),
    ('A_CPSC103', 'B_CPSC101'),
    ('A_CPSC103', 'B_CPSC102'),
    ('A_CPSC103', 'B_CPSC104'),
    ('A_CPSC103', 'C_CPSC102'),
    ('A_CPSC103', 'C_CPSC103'),
    ('B_CPSC101', 'B_CPSC102'),
    ('B_CPSC101', 'B_CPSC104'),
    ('B_CPSC101', 'C_CPSC102'),
    ('B_CPSC101', 'C_CPSC103'),
    ('B_CPSC102', 'B_CPSC104'),
    ('B_CPSC102', 'C_CPSC102'),
    ('B_CPSC102', 'C_CPSC103'),
    ('B_CPSC104', 'C_CPSC102'),
    ('B_CPSC104', 'C_CPSC103'),
    ('C_CPSC102', 'C_CPSC103')
]

# Draw the constraint graph
draw_constraint_graph(binary_constraints)
