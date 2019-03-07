from typing import List
from sim_module import Bug

def test_bug() -> None:

    bugA: Bug = Bug(12, ["C", "A", "C", "T", "T"])
    counta: int = bugA.base_composition("A")
    countc: int = bugA.base_composition("C")
    countg: int = bugA.base_composition("G")

    assert counta == 1, "Error on test 1"
    assert countc == 2, "Error on test 2"
    assert countg == 0, "Error on test 3"

    assert bugA.get_id() == 12, "Error on test 4"


test_bug()
print("tests completed successfully!")
