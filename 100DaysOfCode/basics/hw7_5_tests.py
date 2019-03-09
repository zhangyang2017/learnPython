#!/ACTF/actf_data/packages/python3/3.6.1/bin/python3

from typing import List
from sim_module import Bug, Population

def test_population_cull() -> None:
    popA: Population = Population("genomes_test.txt")
    popA.grow(7, 0.1)
    
    ave_fitness_precull: float = popA.mean_fitness()
    
    popA.cull_to_size(5)
    
    ave_fitness_postcull: float = popA.mean_fitness()
    
    assert popA.get_size() == 5, "Error on test_population_cull 1"
    assert ave_fitness_postcull >= ave_fitness_precull, "Error on test_population_cull 2"
    

test_population_cull()
print("tests completed successfully!")
