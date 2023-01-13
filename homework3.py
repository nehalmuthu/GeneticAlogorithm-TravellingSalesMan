import util
import fitnessUtil
import mutateUtil
import popUtil
import parentCrossUtil

if __name__ == '__main__':
    n,cities=util.tsp_genetic("input.txt")

    if n==1:
        f=open("output.txt", "w")
        s = str(cities[0][0])+" "+str(cities[0][1])+" "+str(cities[0][2])+"\n"
        f.write(s)
        f.close()
        exit()


    # K is no of genomes or paths u wanna create
    #-1 so as  to add greedy heuristic
    k=n
    population=popUtil.generatePopulation(n,k)

    cityDist=util.calcCityDist(n,cities)
    
    # create k paths from greedy heuristic
    # population.extend(util.greedy(n,cityDist))
    greedyPool=[]
    for i in range(k):
        greedyPool.append(util.greedy(i,n,cityDist))
    population.extend(greedyPool)


    mstPool=[]
    for i in range(k//5):
        mstPool.append(util.mst_heuristic(i,n,cityDist))
    population.extend(mstPool)


    iter=n
    for i in range(iter):
        initialpop=population[:]
        #initialpop.extend(population)

        offsprings=parentCrossUtil.chooseParentsandCross(population,cityDist)

        newones=mutateUtil.mutate(offsprings)
        newones.extend(initialpop)

        # how many u wanna choose for next generation
        k=n
        population=fitnessUtil.chooseFitK(newones,k,cityDist)

    res=population[0]
    f=open("output.txt", "w")

    res.append(res[0])
    for i in res:
        s = str(cities[i][0])+" "+str(cities[i][1])+" "+str(cities[i][2])+"\n"
        f.write(s)
    f.close()

