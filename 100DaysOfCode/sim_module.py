#!/ACTF/actf_data/packages/python3/3.6.1/bin/python3

from typing import List, IO
import random
import io, re


class Bug:

    def __init__(self, id: int, genome: List[str]) -> None:
        self.genome: List[str] = genome
        self.id: int = id

    def get_id(self) -> int:
        return self.id

    def base_composition(self, base: str) -> int:
        counter: int = 0

	# item: int
        index: int
        for item in self.genome:
            for index in range(0, len(item)):
                seq_base: str = item[index]
                if base == seq_base:
                    counter = counter + 1
        return counter

    def fitness(self) -> int:
        countT = self.genome.count("T")
        countC = self.genome.count("C")
        countG = self.genome.count("G")
        fit_scores = 3*countT + 2*( countC + countG )
        return fit_scores

    def reproduce(self, mutation_prob: float) -> 'Bug':
        assert mutation_prob >= 0 and mutation_prob <= 1, "Bug reproduce error: mutation_prob not between 0 and 1"
        new_genome: List[str] = []

        bases: List[str] = ["A", "C", "G", "T"]
        rand_el: str = random.choice(bases)

        for i in range(0, len(self.genome)):
            if random.uniform(0,1) < mutation_prob:
                new_genome.append(rand_el)
            else:
                new_genome.append(self.genome[i])

        new_id: int = random.randint(0, 1000000)
        offspring: Bug = Bug(new_id, new_genome)
        return offspring

def bug_fitness(b: Bug) -> float:
    return Bug.fitness(b)


class Population:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.bugs: List[Bug] = []
        
        with io.open(self.name, "r") as fhandle:
            for line in fhandle:
                line = line.strip("\n")
                line_list: List[str] = re.split(r"\s+", line)
                
                id: int = int(line_list[0])
                seqs: str = line_list[1]
                genome = list(seqs)
                newbug: Bug = Bug(id, genome)
                self.bugs.append(newbug)
                

    def get_size(self) -> int:
        return len(self.bugs)

    def mean_fitness(self) -> float:
        scores: List = []
        for bug in self.bugs:
            bug_fitness: int = Bug.fitness(bug)
            scores.append(bug_fitness)
            
        mean = sum(scores) / len(scores)
        return mean
        
    def grow(self, n: int, mutation_prob: float) -> None:
        for i in range(0, n):
            rand_bug = random.choice(self.bugs)
            new_bug = Bug.reproduce(rand_bug, mutation_prob)
            self.bugs.append(new_bug)
            
            
    def cull_to_size(self, n: int) -> None:
        self.bugs.sort(key = bug_fitness)
        assert n <= len(self.bugs), "not enough bugs for reduction !!!"
        self.bugs.reverse()
        self.bugs = self.bugs[0: n]
