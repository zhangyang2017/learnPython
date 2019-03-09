#!/ACTF/actf_data/packages/python3/3.6.1/bin/python3

from typing import List
from sim_module import Bug, Population

def test_population_grow() -> None:
    popA: Population = Population("genomes_test.txt")
    popA.grow(5, 0.1)
    assert popA.get_size() == 8, "Error on test_population_grow 1"
    
test_population_grow()
print("tests completed successfully!")
