#!/ACTF/actf_data/packages/python3/3.6.1/bin/python3

from typing import List
from sim_module import Bug, Population


def test_population() -> None:
    popA: Population = Population("genomes_test.txt")
    popA_size: int = popA.get_size()
    assert popA_size == 3, "Error on test_population 1"
    

test_population()
print("tests completed successfully!")
