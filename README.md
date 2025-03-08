# Task 1
Use the Turtlebot environment that was set up in Programming Project 0 along with the helper code that we provided above to implement the graph search algorithm (similar to best-first search) and make it behave like the following search algorithms:

- Breadth-First Search (BFS)
- Greedy Best First Search (GBFS)
- Uniform Cost Search (UCS)
- A* Search (Astar)
For h(s), use the Manhattan heuristic. Please note that not all of the algorithms in this task might need a heuristic.

# Task 2
Create a line-plot for the time taken to search for a path to the goal by each of the search algorithms in Task 1.

- The x-axis of the plot represents the grid dimension.
- The y-axis of the plot represents the average time taken for each of the grid dimensions (grids with different # of obstacles but the same dimension are to be included when considering the average).
- Each search algorithm will be a different line in the same plot.
The data for generating the plots will be present in the hw1_results.csv file that you will be submitting as a part of the submission instructions detailed in the HTML file provided in the description.

# Task 3
Plot a line-plot for the nodes expanded while searching for a path to the goal by each of the search algorithms in Task 1.
EDIT: Any node with x =-1 or y=-1 should not be expanded. Please refer to the API given in HTML instructions for more details. 

-The x-axis of the plot represents the grid dimension.
-The y-axis of the plot represents the average nodes expanded for each of the grid dimensions (grids with different # of obstacles but the same dimension are to be included when considering the average).
-Each search algorithm will be a different line in the same plot.
The data for generating the plots will be present in the hw1_results.csv file that you will be submitting as a part of the submission instructions detailed in the HTML file provided in the description.
