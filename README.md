# AStarAndFriends
## Introduction
This is an ongoing repo, containing a sequence of search-based path planning algorithms. It will implement several path planning algorithm and visualiza them in a logical order. Detailed comments and explanation are expected as they indicates my learning and interpretation. Hopefully, this might be helpful for you too.
## Search-based path planning
### Overview of the path planning algorithm
Generally, the family of search-based planning algorithms can be classified as classical path planning algorithms, while the intelligent branch contains genetic algorithm, PSO, ACO and so on. While the search-based methods explore the space gradually, another branch of classical methods, the sampling-based methods take random samples and construct the path. A basic and classical example of these algorithms is the rapidly-exploring random tree (RRT).

### Internal connections between search-based method
[![roadmap](images/a.png "roadmap")]
One good start is the breadth-first search, as it contains the essence of search-based planning algorithm. The thoughts of maintaing 2 sets of frontiers and history nodes are fundamental and are widely applied in various cases of more advanced algorithms.
The breadth-first search **uniformly** explores all adjacent nodes. Consequently this introduces large computation cost.  
The Dijkstra`s algorithm and best-first search both consider the priority of the nodes. Dijkstra favors nodes nearer to the start, while Best First Search favors the ones nearer to the goal.  
In unified grid space, where all vacant nodes have the same cost to pass, the Dijkstra performs similarly with the best-first search. But when grids has different properties (like a game`s map), we can see that Dijkstra`s algorithm avoids the nodes with high cost to pass through.


