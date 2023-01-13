import random
import math
import numpy as np
import sys


def calcCityDist(n,cities):
    cityDist= {}
    for i in range(n-1):
        for j in range(i+1,n):
            cityDist[(i,j)]=math.sqrt(sum((np.subtract(cities[i],cities[j]))**2))
    return cityDist


def greedy(start,n,cityDist):
    l=[]
    l.append(start)

    node=start
    iter=n-1
    visit=[0]*n
    visit[start]=1
    while iter:
        mini=sys.maxsize
        next=node
        for i in range(n):
            ky=[node,i]
            ky.sort()
            if i!=node and visit[i]==0 and cityDist[tuple(ky)]<mini:
                mini = cityDist[tuple(ky)]
                next=i
        node=next
        visit[node]=1
        l.append(next)
        iter-=1
    return l


def mst_heuristic(start,n,cityDist):

    INF=sys.maxsize
    selected_node = [0]*n

    no_edge = 0
    l=[]
    l.append(start)

    selected_node[start] = True
    while (no_edge < n - 1):
        minimum = INF
        b = 0
        for m in range(n):
            if selected_node[m]:
                for i in range(n):
                    ky=[m,i]
                    ky.sort()
                    if ((not selected_node[i])):
                        if minimum > cityDist[tuple(ky)]:
                            minimum = cityDist[tuple(ky)]
                            b = i
        l.append(b)
        selected_node[b] = True
        no_edge += 1
    return l


# read input file
# converts the 3d location from file to list of lists
def tsp_genetic(input):
    f=open(input,"r")
    s=f.readlines()
    f.close()
    l=[]
    # getting no of cities from file
    n=int(s[0].split()[0])
    # convert 3 d locations to list of lists
    for i in range(1,len(s)):
        l.append(list(map(int, s[i].split())))

    return n,l

