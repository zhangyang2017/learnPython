#!/ACTF/actf_data/packages/python3/3.6.1/bin/python3

from typing import List
from sim_module import Bug, Population

def test_population_mean() -> None:
    popA: Population = Population("genomes_test.txt")
    popA_mean: float = popA.mean_fitness()
    known_mean: float = (4*2 + 1*2 + 4*3) / 3
    
    assert abs(popA_mean - known_mean) < 0.000001, "Error on test_population 1"
    
    
test_population_mean()
print("tests completed successfully!")
