# My solution to the LIA problem
# The Organism class stores alleles in a list of n lists, with n being th enumber of genes, and can reproduce() with another organism, returning a new organism with a random allele that each parent has for each gene.
# Generations store Organisms, and can advance_generations(), returning a generation of the children of each of its organisms and an Aa-Bb mate, according to he problem.
# We use a Monte-Carlo method to approximate the probability in a high number of simulations.
# We run make_generation_k at each simulation to go to the k-th generation.

from random import randint
class Organism():
    def __init__(self, *alleles):
       self.alleles = alleles 

    def reproduce(self, mate):
        passed_alleles = []
        for i in range(len(self.alleles)):
            passed_alleles.append([self.alleles[i][randint(0,1)], mate.alleles[i][randint(0,1)]])
        return Organism(*passed_alleles)

class Generation():
    def __init__(self, *organisms):
        self.population = [organism for organism in organisms]

    def advance_generation(self, offsprings=2):
        new_organisms = []
        for organism in self.population:
            for i in range(offsprings):
                child = organism.reproduce(mate)
                new_organisms.append(child)
        return Generation(*new_organisms)


def make_generation_k(k, gen0):
    current_gen = gen0
    for i in range(k):
        current_gen = current_gen.advance_generation()
    return current_gen
        

if __name__ == "__main__":
    mate = Organism(["A", "a"], ["B", "b"])
    gen0 = Generation(mate)
    k = int(input("k? "))
    n = int(input("n? "))
    number_of_sims = 100000
    result = 0
    for i in range(number_of_sims):
        number_AaBb = 0 # number of individuals with the correct genotype
        last_gen = make_generation_k(k, gen0)
        if i > 0:
            print(round(i/1000, 2), "% done, current probability is", result/i)
        for j in last_gen.population:
            if ("A" in j.alleles[0]) and ("a" in j.alleles[0]) and ("B" in j.alleles[1]) and ("b" in j.alleles[1]):
                number_AaBb += 1
        if number_AaBb >= n:
            result +=1
    print("Finished, probability is estimated to:", result/number_of_sims)
