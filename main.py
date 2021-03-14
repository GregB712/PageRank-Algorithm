# Importing needed libraries.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Importing needed python scripts.
import PageRank as PR
import GraphCreation as GC

if __name__ == '__main__':
        
        # The graph's data
        number_of_nodes = 100 # number of nodes
        p = 0.4 # probability of edge existence
        G = GC.ER(number_of_nodes, p)

        # Draw the graph
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        plt.title("Random Graph Generation")
        plt.show()

        d = 0.85 # damping factor
        error = 0.00001 # acceptable error (for converge)

        L = np.zeros(shape=(number_of_nodes,number_of_nodes))
        for j in range(number_of_nodes):
                for i in range(number_of_nodes):
                        if i in list(G.successors(j)):
                                L[j][i] = 1/G.out_degree(j)

        ranking1 = PR.pageRanking(number_of_nodes, error, L)

        ranking2 = PR.PR_DF(number_of_nodes, error, L, d)