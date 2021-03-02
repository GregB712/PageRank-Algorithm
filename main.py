import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import PageRank as PR
import GraphCreation as GC

if __name__ == '__main__':
        
        # The graph's data
        nodes = 1000
        p = 0.4
        G = GC.ER(nodes, p)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        plt.title("Random Graph Generation Example")
        plt.show()

        d = 0.3 # constant

        L = np.zeros(shape=(nodes,nodes))
        for j in range(nodes):
                for i in range(nodes):
                        if i in list(G.successors(j)):
                                L[j][i] = 1/G.out_degree(j)

        ranking1 = PR.pageRanking(nodes, 0.001, L)
        ranking2 = PR.PR_DF(nodes, 0.01, L, 0.3)
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