import requests
from collections import defaultdict
import random

mstGraph= {}
vis =[]
travelRoute = []


class Node:
    def __init__(self,idx,dist):
        self.idx = idx
        self.dist = dist
        
class Edge:
    def __init__(self,u,v,dist):
        self.u = u
        self.v = v
        self.dist = dist

def initDistances(address, destAddress):
    pickMatrix = [[0 for x in range(len(address))] for y in range(len(address))] 
    dropMatrix = [[0 for x in range(len(destAddress))] for y in range(len(destAddress))] 
    pickDropDist =[]
    for i in range(0,len(address)):
        for j in range(0,len(address)):
            if i==j: continue
            if pickMatrix[j][i]!=0:
                pickMatrix[i][j]=pickMatrix[j][i]
            else:
                print(address[i],address[j])
                pickMatrix[i][j]= getDist(address[i],address[j])


    print()

def mstClear():
    global mstGraph
    global vis
    global travelRoute
    mstGraph=[]
    vis=[]
    travelRoute=[]


#use Google Maps API to find time required to travel between 2 points
def getDist(startP,endP):
    # API key
    api_key = ''
    # base url
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    # get response
    r = requests.get(url + "origins=" + startP + "&destinations=" + endP + "&key=" + api_key) 
    # return time as text and as seconds
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return [time,seconds]

def createGraph(address):
    graph=defaultdict(set)
    for i in range(0,len(address)):
        print(i,"-->",end='')
        for j in range (i+1,len(address)):
            d = random.randint(10,100);
            try:graph[i].append(Node(j,d))
            except:graph.update({i:[Node(j,d)]})
            try:graph[j].append(Node(i,d))
            except:graph.update({j:[Node(i,d)]})
        for k in range(0,len(graph[i])):
            print("{",graph[i][k].idx,",",graph[i][k].dist,"}",end=' ')
        print()
    return graph

def minSpanningTree(graph,n):
    edges = []
    tree_id =[]
    for i in range(0,n):
        tree_id.append(i)
    for i in range (0,len(graph)):
        for j in range (0,len(graph[i])):
            edges.append(Edge(i,graph[i][j].idx,graph[i][j].dist))
    sortEdges = sorted(edges,key=lambda x:x.dist)
    print("Sorted Edges-->",end=" ")
    for i in range (0,len(edges)):
        print(sortEdges[i].dist,end=' ');
    print()
    mstEdges=[]
    for edge in sortEdges:
        if(tree_id[edge.u]!=tree_id[edge.v]):
            mstEdges.append(edge)
        oldp = tree_id[edge.u]
        newp = tree_id[edge.v]
        for i in range(0,n):
            if(tree_id[i] == oldp):
                tree_id[i]= newp
    print("MST Edges-->",end=" ")
    for i in range(0,len(mstEdges)):
        print("(",mstEdges[i].u,",",mstEdges[i].v,") -->",mstEdges[i].dist,end=' ')
    print()
    mst={}
    for e in mstEdges:
        try:mst[e.u].append(Node(e.v,e.dist))
        except:mst.update({e.u:[Node(e.v,e.dist)]})
        try:mst[e.v].append(Node(e.u,e.dist))
        except:mst.update({e.v:[Node(e.u,e.dist)]})
    return mst


def dfs(node):
    travelRoute.append(node)
    vis[node]=True
    for e in mstGraph[node]:
        if vis[e.idx]==False:
            dfs(e.idx)
            travelRoute.append(node)

def getTravelRoute(mst,n):
    for i in range(0,n):
        vis.append(False)
    global mstGraph
    mstGraph=mst
    dfs(0)
    print("TravelRoute-->",end=" ")
    for i in range(0,len(travelRoute)):
        print(travelRoute[i],end=' ')
    print()
    return travelRoute

def calculateCost():
    print()





