import numpy as np
import pandas as pd
import PageRank as PR

if __name__ == '__main__':
    # The graph's data

    number_of_nodes = 4
    la = np.array([0,1/3,1/3,1/3])
    lb = np.array([1/2,0,0,1/2])
    lc = np.array([0,0,0,1])
    ld = np.array([0,1/2,1/2,0])

    L = np.matrix([la,lb,lc,ld]).transpose()

    d = 0.3 # constant

    #print(L)

    data = {'Node':['A', 'B', 'C', 'D'], 
            'Outgoing':[3, 2, 2, 1],
            'Showing': [['B','C','D'], ['A','C'], ['B','D'], ['C']],
            'Ranking':[1/number_of_nodes,1/number_of_nodes,1/number_of_nodes,1/number_of_nodes]
            }

    graph_df = pd.DataFrame(data)

    ranking = PR.pageRanking(4, 0.01, L)

    print("---------------------------------------------------------------")

    graph_df['Ranking'] = ranking
    print(graph_df)