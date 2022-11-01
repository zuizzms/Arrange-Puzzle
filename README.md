# The-Eight-Puzzle

Many problems can be framed as a search for a series of actions that take you from some initial state to some goal state. Examples include robot navigation, route finding, and map labeling. For such a problem, the state space of the problem is the collection of all states that can be reached by starting in the initial state and applying some number of actions. State-space search is the technical term given to the process of searching through the state space for a path to the goal state, and many different algorithms have been developed for that process.

The project involves applying state-space search to a classic problem known as the Eight Puzzle, which we’ve discussed in lecture. The Eight Puzzle is a 3x3 grid containing 8 numbered tiles and one empty or blank cell. 
Here is one possible configuration of the tiles, with the blank cell shown shaded blue:

![image](https://user-images.githubusercontent.com/50706134/194730803-c38c069d-5c6a-4820-baf7-fe333d4b5c2d.png)

Tiles that are adjacent to the blank cell can move into that position in the grid, and solving the puzzle involves moving the tiles until you reach the following goal state:

![image](https://user-images.githubusercontent.com/50706134/194730818-b266c3b2-194d-41e1-a1d3-1ce9dce381db.png)

This project applies state space search to solve any valid initial configuration of the Eight Puzzle.

A puzzle is represented by a string of digits, where the 0 represents the blank space. For example, "142358607" would represent the board:

![image](https://user-images.githubusercontent.com/50706134/194731223-77ec200a-763d-4d3e-9e76-3a9f29c17a78.png)

The file results.txt compares search algorithms and highlights each algorithm's performance when solving puzzles that are different lengths away from being solved.

The algorithms compared include:
- Random Search: randomly applies state-space search
- Breadth First Search (BFS): chooses one the untested states that has the smallest depth (i.e., the smallest number of moves from the initial state)
- Depth First Search (DFS): chooses one the untested states that has the largest depth (i.e., the largest number of moves from the initial state)
- Greedy Search: informed search algorithm that uses a heuristic function to estimate the remaining cost needed to get from a given state to the goal state (for the Eight Puzzle, this is just an estimate of how many additional moves are needed). Greedy Search uses this heuristic function when computing the priority of each state, and it selects the next state based on those priorities
- A* Search: informed search algorithm that assigns a priority to each state based on a heuristic function, and that selects the next state based on those priorities. However, when A* assigns a priority to a state, it also takes into account the cost that has already been expended to get to that state (i.e. the number of moves to that state)


