# Gallagher-Humblet-Spira algorithm in DistAlgo
Implementation of the Gallagher-Humblet-Spira algorithm in DistAlgo (Python) for the INF571 Distributed Computing course.<br>
See *presentation.pdf* for more info.

### How to run it
Open a terminal in the root folder of the project and run the command
```
python -m da ghs.da
```
A random graph will be generated and shown; then, the algorithm will run on it and, when it terminates, the spanning tree will be shown.


### Known bugs
The input graph is generated using igraph's *Erdos_Renyi* function. Sometimes, the generated graph is not connected and this may lead the GHS algorithm to get stuck. If this happens, please run again the algorithm to generate a new graph until a connected graph is generated.

#### Using a specific input graph
If you want to run the *GHS Algorithm* on a specific graph instead of a randomly generated one, you have to modify lines 305, 313 and 314 of the code:
- Specify the number of nodes of your graph in line 305
- Specify the list of edges in your graph in line 313, replacing the call to *genGraphEdges()* function. This list should be a list of tuples (i,j) that represent edges of the graph.
- Specify the list of edges' weights: a list of natural numbers, one for each tuple (edge) of the *topo* list (in the same order).

```
[305] NUM_NODES = 5
...
[313] topo = [(0,1), (1,2), (3,2), (1,4), (0,3), (4,2), (4,3), (4,0)]
[314] weights = [1,2,3,4,5,6,7,8]
```

