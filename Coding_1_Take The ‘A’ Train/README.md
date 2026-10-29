# Take the 'A' Train

This project implements a train-yard search problem in Python using classic AI search techniques. The goal is to model train movements on a set of tracks and solve the arrangement problem using breadth-first search and A* search.

## Overview

The code in `YardSearcher.py` defines a `YardSearcher` class that:

- models the yard layout and train-car arrangement
- generates valid actions for each state
- applies actions to produce new states
- solves the problem using uninformed search (BFS)
- uses an admissible heuristic and A* search for more efficient planning

## Project files

- `YardSearcher.py` — main implementation of the search logic
- `test.py` — command-line test runner for the assignment
- `tests/` — unit tests for each question/problem
- `yards/` — example yard configurations
- `COLLABORATION.md` — collaboration and resource acknowledgments

## Run the program

```bash
python YardSearcher.py
```

This runs the sample yard scenario and prints the resulting path to the goal, along with the number of nodes explored.

## Run tests

Run the full assignment test suite:

```bash
python test.py
```

Run only selected questions:

```bash
python test.py -q q1 q2 q3 q4 q6
```

The available test groups are:

- `q1` — possible actions
- `q2` — result function
- `q3` — action sequence application
- `q4` — uninformed search
- `q5` — heuristic function
- `q6` — A* search

## Assignment context

This assignment focuses on:

- state representation and transition modeling
- search-space exploration
- admissible heuristics
- optimal path finding with BFS and A* search

## Notes

The repository includes the assignment PDF and supporting materials, but the core implementation and tests are contained in the Python files above.