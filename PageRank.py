# Importing needed libraries.
import numpy as np
import time

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
      #print("We needed: ",i, " iterations")
      #print(temp)
      #print("Rankings are: ", r)
      #print(temp-r)
      break
    temp = r
    r = np.dot(L,r) # Dot product between L and r
    r = np.squeeze(np.asarray(r)) # Flatten the r (the dot product is type matrix, we need array)
    if all(abs(element) < acceptable_error for element in temp-r): # Check for converge
      temp_boolean = False
    
  end = time.time()
  duration = end - start
  print("We needed: ",i, " iterations")
  print("Rankings are: ", r)
  print("Duration: ",duration*1000, "ms")

  return r

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
  print("We needed: ",i, " iterations")
  print("Rankings are: ", temp)
  print("Duration: ",duration*1000, "ms")

  return r