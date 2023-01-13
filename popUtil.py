import random

#generates a random path from n for population
def generatePath(n):
    return random.sample(range(0,n),n)

#genertae population
#here we are generating 10 genomes
def generatePopulation(n,k):
    population=[]
    for i in range(k):
        population.append(generatePath(n))
    return population
