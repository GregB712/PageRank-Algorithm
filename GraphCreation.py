# Importing needed libraries.
import networkx as nx
from itertools import combinations
from random import random

def ER(number_of_nodes, p):
    """
    Base code from https://compucademy.net/generating-random-graphs-in-python/
    The algorithm uses the Erdős–Rényi model.
    Given number of nodes and propability of vertex existence creates a random directed graph.

    Parameters:
    number_of_nodes (Int): The number of the graph's nodes.
    p (float): The existentially propability of each vertex between the nodes.

    Returns:
    g (DiGraph): A directed graph (Object of the DiGraph class).
    """
    V = set([v for v in range(number_of_nodes)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    g = nx.DiGraph()
    g.add_nodes_from(V)
    g.add_edges_from(E)

    return g