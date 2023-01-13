def calcPathDist(path,cityDist):
    #has to end at starting node
    # so appending it
    #path.append(path[0])
    dist=0
    for i in range(len(path)-1):
        id=[path[i],path[i+1]]
        id.sort()
        dist += cityDist[tuple(id)]
    #end at starting node - adding cost for that
    id=[path[0],path[i]]
    id.sort()
    dist += cityDist[tuple(id)]
    return dist


def calcFitness(population,cityDist):
    fitness=[]
    pop=population[:]
    for i in range(len(pop)):
        fitness.append(calcPathDist(pop[i],cityDist))
    return fitness

# from population+newone - choose top fittest k
#here k=10
def chooseFitK(population,k,cityDist):

    fitness = calcFitness(population,cityDist)


    #create a list of index - range(len)
    #sort it by fitness[i]
    # so u r sorting i by fitness[i]
    # we get ascending order and that what we need - min sitness means least cost

    pop_index=sorted(range(len(fitness)), key=lambda i: fitness[i])[:k]
    pop_index.sort()

    print(min(fitness))
    return [population[i] for i in pop_index]


