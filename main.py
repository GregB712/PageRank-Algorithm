# Importing needed libraries.
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Importing needed python scripts.
import PageRank as PR
import GraphCreation as GC

if __name__ == '__main__':
        
        # The graph's data
        number_of_nodes = 10
        p = 0.4
        G = GC.ER(number_of_nodes, p)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        plt.title("Random Graph Generation Example")
        plt.show()

        d = 0.3 # dumping factor
        error = 0.01 # acceptable error

        L = np.zeros(shape=(number_of_nodes,number_of_nodes))
        for j in range(number_of_nodes):
                for i in range(number_of_nodes):
                        if i in list(G.successors(j)):
                                L[j][i] = 1/G.out_degree(j)

        ranking1 = PR.pageRanking(number_of_nodes, error*10, L)

        ranking2 = PR.PR_DF(number_of_nodes, error, L, d)
        #print(L)

        #data = {'Node':['A', 'B', 'C', 'D'], 
        #        'Outgoing':[3, 2, 2, 1],
        #        'Showing': [['B','C','D'], ['A','C'], ['B','D'], ['C']],
        #        'Ranking':[1/number_of_nodes,1/number_of_nodes,1/number_of_nodes,1/number_of_nodes]
        #        }

        #graph_df = pd.DataFrame(data)

        #ranking = PR.pageRanking(4, 0.01, L)

        #print("---------------------------------------------------------------")

        #graph_df['Ranking'] = ranking
        #print(graph_df)