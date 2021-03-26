### *Graph Theory 2020, 8th Semester of Computer Science and Software Engineering Division @ Mälardalens högskola*

## PageRanking Algorithm

#### Decription:
Today we live in the world of big data. Information for anything is just one click away. But the data are not always physically sorted. We mostly encounter them distributed in millions of sites. Also they are subject to constant changes and they are repeated. We cannot be sure about the quality of each source and moreover there is a vast heterogeneity among them, i.e. you can find them as html, pdf, mpg and so on. 
To deal with those problems in the World Wide Web (WWW) we have created search engines that can take a query as an input and return the desired information. In order to succeed both query and not query ranking algorithms are being used. An example of a query independent algorithm is the PageRank.

The concept of this project is to test some implementations of the PageRanking methods and try them on some sample graphs in a programming environment.
More specifically in this project the simple and the damping factor algorithm are compared using the power method to speed up the results.

In order to run the code below the following libraries are needed:
- numpy
- matplotlib
- time
- multiprocessing
- scipy
- networkx
- itertools
- random
Also regarding the version python, 3.x (preferable 3.7.x +) is suggested.

We are dealing with 4 distinct scripts:
- main.py:
Script for single graph creation and implementation of PageRank algorithms.
- main2.py:
Script that returns some plots about the comparisons of the two variations of the PageRank algorithm.
- GraphCreation.py:
We use the Erdős–Rényi model. Given a number of nodes and probability of vertex existence creates a random directed graph.
- PageRank.py:
The script with the two PageRank Algorithms
