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
      break
    temp = r
    r = np.dot(L,r) # Dot product between L and r
    r = np.squeeze(np.asarray(r)) # Flatten the r (the dot product is type matrix, we need array)
    if all(abs(element) < acceptable_error for element in temp-r): # Check for converge
      temp_boolean = False
    
  end = time.time()
  duration = end - start
  r = [np.format_float_scientific(i, unique=False, precision=15) for i in r] # Fixing the accuracy
  print("We needed: ",i, " iterations")
  print("Rankings are: ", [sorted(r).index(x) for x in r]) # Rankings (integer numbers)
  print("Duration: ",duration*1000, "ms")

  return r

# Page ranking with damping factor
def PR_DF(number_of_nodes, acceptable_error, L, damping):
  """
  Giving L the function will perform the Page Ranking algorithm using the damping factor in the formula
  returning the results as a list.

  Parameters:
  number_of_nodes (Int): The number of the graph's nodes.
  acceptable_error (float): Threshold for converge in order to stop in a specific number of iterations.
  L (numpy array): A matrix with the initialized scores that each node give to each other.
  damping (float): The damping factor of the algorithm.

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
    r = (1-damping)/number_of_nodes + damping*np.dot(L,r) # Dot product between L and r
    r = np.squeeze(np.asarray(r)) # Flatten the r (the dot product is type matrix, we need array)
    if all(abs(element) < acceptable_error for element in temp-r): # Check for converge
      temp_boolean = False
    
  end = time.time()
  duration = end - start
  temp = [q*100 for q in r]
  temp = [np.format_float_scientific(i, unique=False, precision=15) for i in temp] # Fixing the accuracy
  print("We needed: ",i, " iterations")
  print("Rankings are: ", [sorted(temp).index(x) for x in temp]) # Rankings (integer numbers)
  print("Duration: ",duration*1000, "ms")

  return r