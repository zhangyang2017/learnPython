#!/ACTF/actf_data/packages/python3/3.6.1/bin/python3

from sim_module import Population

pop: Population = Population("genomes.txt")

i: int
for i in range(0, 100):
    pop.grow(10, 0.1)
    pop.cull_to_size(100)
    print(str(i) + "\t" + str(pop.mean_fitness()))
