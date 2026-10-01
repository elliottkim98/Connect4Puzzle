# Eight Puzzle Search Algorithms

A Python implementation of state-space search techniques for solving the classic **8-puzzle**. The project compares uninformed and informed search strategies and measures how different heuristics affect search efficiency.

## Features

- Random state-space search
- Breadth-First Search (BFS)
- Depth-First Search (DFS) with optional depth limits
- Greedy Search
- A* Search
- Cycle detection
- Solution-path reconstruction
- Runtime and states-tested measurements
- Batch processing of puzzle sets with different optimal solution lengths

## Heuristics

The informed search algorithms support two heuristics:

- **h1 — Misplaced tiles:** counts tiles that are not in their goal positions.
- **h2 — Manhattan distance:** sums each tile's row and column distance from its goal position.

## Project Structure

```text
Eight-Puzzle-Search/
├── board.py          # Board representation and heuristic helpers
├── state.py          # Search-state representation and successor generation
├── searcher.py       # Random, BFS, DFS, Greedy, and A* searchers
├── eight_puzzle.py   # Driver functions for solving and benchmarking puzzles
├── timer.py          # Runtime utility
├── results.txt       # Recorded benchmark results
├── data/
│   ├── 5_moves.txt
│   ├── 10_moves.txt
│   ├── 15_moves.txt
│   ├── 18_moves.txt
│   ├── 21_moves.txt
│   ├── 24_moves.txt
│   └── 27_moves.txt
└── README.md
```

## Running the Project

Requires **Python 3** and no external packages.

Start Python from the repository directory:

```bash
python3
```

Then import the project:

```python
from eight_puzzle import *
```

### Solve a puzzle with BFS

```python
eight_puzzle('142075368', 'BFS')
```

### Solve with A* and Manhattan distance

```python
eight_puzzle('142075368', 'A*', heuristic=h2)
```

### Process a benchmark file

```python
process_file('data/15_moves.txt', 'A*', heuristic=h2)
```

## Results

The benchmark experiments show how search strategy and heuristic choice affect the number of states explored. In the recorded tests, A* with the Manhattan-distance heuristic (`h2`) consistently solved the supplied benchmark sets and generally explored far fewer states than A* with the misplaced-tiles heuristic (`h1`) on harder puzzles.

For example, on the 27-move benchmark set:

| Algorithm | Heuristic | Puzzles Solved | Avg. States Tested |
|---|---|---:|---:|
| Greedy | h1 | 2 / 10 | 1,270.5 |
| Greedy | h2 | 10 / 10 | 418.8 |
| A* | h1 | 0 / 10 | — |
| A* | h2 | 10 / 10 | 12,304.8 |

See [`results.txt`](results.txt) for the full benchmark output.

## What I Learned

This project strengthened my understanding of:

- State-space search and search trees
- BFS and DFS traversal strategies
- Greedy versus A* search
- Designing and evaluating heuristic functions
- Cycle detection and search-depth constraints
- Measuring algorithm performance through runtime and states explored

## Author

**Elliott Kim**
