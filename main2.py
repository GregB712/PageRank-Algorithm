# Importing needed libraries.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from multiprocessing import Pool
import time
from scipy.signal import savgol_filter

# Importing needed python scripts.
import GraphCreation as GC

def pageRanking(number_of_nodes, acceptable_error, L):
  """
  Giving L the function will perform the basic Page Ranking algorithm returning the results as a list.

  Parameters:
  number_of_nodes (Int): The number of the graph's nodes.
  acceptable_error (float): Threshold for converge in order to stop in a specific number of iterations.
  L (numpy array): A matrix with the initialized scores that each node give to each other.

  Returns:
  r (List): The result list with the rankings for each node.
  """
  start = time.time()
  r = np.full((1, number_of_nodes), 1/number_of_nodes)
  r = np.squeeze(np.asarray(r)) # Flatten the matrix. From [[0]] to [0].

  number_of_iterations = 100 # We use this variable as a safety valve for avoiding infinite loops.
  temp_boolean = True

  for i in range(number_of_iterations):
    if (temp_boolean == False): # Stop if there is converge
      break
    temp = r
    r = np.dot(L,r) # Dot product between L and r
    r = np.squeeze(np.asarray(r)) # Flatten the r (the dot product is type matrix, we need array)
    if all(abs(element) < acceptable_error for element in temp-r): # Check for converge
      temp_boolean = False
    
  end = time.time()
  duration = end - start
  r = [np.format_float_scientific(i, unique=False, precision=15) for i in r]
  ranks = [sorted(r).index(x) for x in r]

  return r, i, ranks, duration*1000

# Page ranking with dumping factor
def PR_DF(number_of_nodes, acceptable_error, L, dumping):
  """
  Giving L the function will perform the Page Ranking algorithm using the dumping factor in the formula
  returning the results as a list.

  Parameters:
  number_of_nodes (Int): The number of the graph's nodes.
  acceptable_error (float): Threshold for converge in order to stop in a specific number of iterations.
  L (numpy array): A matrix with the initialized scores that each node give to each other.
  dumping (float): The dumping factor of the algorithm.

  Returns:
  r (List): The result list with the rankings for each node.
  """
  start = time.time()
  r = np.full((1, number_of_nodes), 1/number_of_nodes)
  r = np.squeeze(np.asarray(r)) # Flatten the matrix. From [[0]] to [0].

  number_of_iterations = 100 # We use this variable as a safety valve for avoiding infinite loops.
  temp_boolean = True

  for i in range(number_of_iterations):
    if (temp_boolean == False): # Stop if there is converge
      break
    temp = r
    r = (1-dumping)/number_of_nodes + dumping*np.dot(L,r) # Dot product between L and r
    r = np.squeeze(np.asarray(r)) # Flatten the r (the dot product is type matrix, we need array)
    if all(abs(element) < acceptable_error for element in temp-r): # Check for converge
      temp_boolean = False
    
  end = time.time()
  duration = end - start
  temp = [q*100 for q in r]
  temp = [np.format_float_scientific(i, unique=False, precision=15) for i in temp]
  ranks = [sorted(temp).index(x) for x in temp]

  return r, i, ranks, duration*1000

def loop_logs(number_of_nodes):
    p = np.log(number_of_nodes)/number_of_nodes
    G = GC.ER(number_of_nodes, p)

    L = np.zeros(shape=(number_of_nodes,number_of_nodes))
    for j in range(number_of_nodes):
            for i in range(number_of_nodes):
                    if i in list(G.successors(j)):
                            L[j][i] = 1/G.out_degree(j)

    s, iterations, r, duration = pageRanking(number_of_nodes, error, L)

    return iterations,duration,number_of_nodes

def loop_logs_D(number_of_nodes):
    p = np.log(number_of_nodes)/number_of_nodes
    G = GC.ER(number_of_nodes, p)

    L = np.zeros(shape=(number_of_nodes,number_of_nodes))
    for j in range(number_of_nodes):
            for i in range(number_of_nodes):
                    if i in list(G.successors(j)):
                            L[j][i] = 1/G.out_degree(j)

    s, iterations, r, duration = PR_DF(number_of_nodes, error, L, d)

    return iterations,duration,number_of_nodes

def create_plots(my_array, my_string):
  plt.rcParams["figure.figsize"] = (20,10)
  fig, (ax1, ax2) = plt.subplots(1, 2)

  fig.suptitle(my_string)
  x = my_array[:,2]
  duration = my_array[:,1] # duration
  iterations = my_array[:,0] # iterations
  yhat1 = savgol_filter(duration, 51, 3) # window size 51, polynomial order 3
  yhat2 = savgol_filter(iterations, 51, 3)

  ax1.set_title('Durations vs Nodes')
  ax2.set_title('Iterations vs Nodes')
  ax1.set(xlabel='# Nodes', ylabel='# Milliseconds')
  ax2.set(xlabel='# Nodes', ylabel='# Iterations')
  #ax1.plot(x, duration)
  #ax2.plot(x, iterations)
  ax1.plot(x,yhat1, color='red')
  ax2.plot(x,yhat2, color='red')
  plt.show()

if __name__ == '__main__':
    d = 0.85 # damping factor
    error = 0.0000001 # acceptable error

    pool = Pool(processes=10)

    number_of_nodes = range(2,1000,4)

    simple_pr = np.array(pool.map(loop_logs, number_of_nodes))

    print('Done with simple pr')

    dumping_pr = np.array(pool.map(loop_logs_D, number_of_nodes))

    print('Done with df-pr')

    pool.close() # ATTENTION HERE

    create_plots(simple_pr, "Normal Page Ranking")

    create_plots(dumping_pr, "Damping Factor Page Ranking")