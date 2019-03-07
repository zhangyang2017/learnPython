#!/ACTF/actf_data/packages/python3/3.6.1/bin/python3
from typing import List
from sim_module import Bug, Population, bug_fitness

def test_bug_fitness_func() -> None:
    bugA: Bug = Bug(1, ["C", "A", "C", "T", "T"])
    
    assert bug_fitness(bugA) == bugA.fitness(), "Error with bug fitness function"
    
    
test_bug_fitness_func()
print("tests completed successfully!")
