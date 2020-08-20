# MetaheuristicOptimization

## Description
- In Function Optimization folder:
1. Random Search: Implemented a random search method as an optimizer, and tested it on the toy problems from main.py. The initialization point for the method is to be set to (x,y)=(15,15).
2. Gradient Descend: Implemented a gradient descend (or steepest descend) method as an optimizer, and tested it on the toy problems from main.py. The initialization point for the method is to be set to (x,y)=(15,15).
3. Newton-Raphson method: Descend: Implemented a Newton-Raphson method as an optimizer, and tested it on the toy problems from main.py. The initialization point for the method is to be set to (x,y)=(15,15).

- In TSP problems:
1. main.py: **Travel in a loop:** The salesman travels in a loop. A loop of length X refers to a tour of X cities, where the salesman returns to the original city after visiting the last (a closed loop).
Example: for a loop of length four, the itinerary might look as follows [1, 2, 3, 4]. But, in reality, the class calculates the length with return to 1.
2. RandomSearch.py: Implemented a random search for the problem.
3. ExhaustiveSearch.py: Implemented a Exhaustive search for the problem.
4. GeneticAlg.py: Implemented a Genetic algorithm for the problem.
5. DifferentialAlg.py: Implemented a Differential Evolution algorithm for the problem.
