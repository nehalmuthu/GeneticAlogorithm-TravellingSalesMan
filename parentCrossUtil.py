#just one point cross
#for 2nd offspring reversed second part
def cross(parent1,parent2):
    n=int(len(parent1)/2)
    for i in range(0,n):
        parent2.remove(parent1[i])
    parent1[n:]=parent2
    #first it was reverse now  removed it for reducing time
    parent2.extend(parent1[:n])
    return parent1, parent2


def chooseParentsandCross(population,cityDist):
    offsprings=[]
    # sorting population by fitness score
    #fit = util.calcFitness(population,cityDist)
    #population = [x for _,x in sorted(zip(fit,population))]


    #genetae population in even numbers
    for i in range(len(population)-1):
        # [:] means shallow copy
        p1=population[i][:]
        p2=population[i+1][:]
        offspring1,offspring2=cross(p1,p2)
        offsprings.append(offspring1)
        offsprings.append(offspring2)

    return offsprings

