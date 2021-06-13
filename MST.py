import requests
from collections import defaultdict
import random
from clientss import *

mstGraph= {}
vis =[]
travelRoute = []
pickMatrix = []
dropMatrix = []
pickDropDist =[]

#Nodes are used in graph networks to represent a location
class Node:
    def __init__(self,idx,dist):
        self.idx = idx
        self.dist = dist
        
#Edges are used in graph networks to represent roads between 2 locations
class Edge:
    def __init__(self,u,v,dist):
        self.u = u
        self.v = v
        self.dist = dist

#This uses the Google Maps API to determine distances between all N pairs of clients, used to calcuate realtime data
def initDistances(address, destAddress):
    global pickMatrix
    global dropMatrix
    global pickDropDist

    pickMatrix = [[0 for x in range(len(address))] for y in range(len(address))] 
    dropMatrix = [[0 for x in range(len(destAddress))] for y in range(len(destAddress))] 

    for i in range(0,len(address)):
        for j in range(0,len(address)):
            if i==j: continue
            if pickMatrix[j][i]!=0:
                pickMatrix[i][j]=pickMatrix[j][i]
            else:
                #print(address[i],address[j])
                pickMatrix[i][j]= getDist(address[i],address[j])

    for i in range(0,len(destAddress)):
        for j in range(0,len(destAddress)):
            if i==j: continue
            if dropMatrix[j][i]!=0:
                dropMatrix[i][j]=dropMatrix[j][i]
            else:
                #print(destAddress[i],destAddress[j])
                dropMatrix[i][j]= getDist(destAddress[i],destAddress[j])
    
    for i in range(0,len(address)):
        pickDropDist.append(getDist(address[i],destAddress[i]))
    
# Clears the Minimum Spanning Tree
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
    api_key = API_KEY
    # base url
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    # get response
    r = requests.get(url + "origins=" + startP + "&destinations=" + endP + "&key=" + api_key) 
    # return time as text and as seconds
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
    dist = (r.json()["rows"][0]["elements"][0]["distance"]["value"])/1000
    return [time,dist]

#Uses client locations to create a graph data structure
#This graph has (N)(N-1) edges, and is converted to a tree with N-1 edges using the Minumum Spanning Tree Algorithm
def createGraph(address,num):
    graph=defaultdict(set)
    for i in range(0,len(address)):
        print(i,"-->",end='')
        for j in range (i+1,len(address)):
            d=0
            if num ==0:
                d = pickMatrix[i][j][0]
            elif num==1:
                d = dropMatrix[i][j][0]
            try:graph[i].append(Node(j,d))
            except:graph.update({i:[Node(j,d)]})
            try:graph[j].append(Node(i,d))
            except:graph.update({j:[Node(i,d)]})
        #for k in range(0,len(graph[i])):
            #print("{",graph[i][k].idx,",",graph[i][k].dist,"}",end=' ')
        #print()
    return graph

#Creates a Minimum Spanning Tree of client locations to minimize the distance the driver has to travel
#The drivers only uses the roads in this tree to get to clients
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
    #for i in range(0,len(mstEdges)):
        #print("(",mstEdges[i].u,",",mstEdges[i].v,") -->",mstEdges[i].dist,end=' ')
    #print()
    mst={}
    for e in mstEdges:
        try:mst[e.u].append(Node(e.v,e.dist))
        except:mst.update({e.u:[Node(e.v,e.dist)]})
        try:mst[e.v].append(Node(e.u,e.dist))
        except:mst.update({e.v:[Node(e.u,e.dist)]})
    return mst

#Depth-first search is used to create a route (an array of points) to travel between locations
def dfs(node):
    travelRoute.append(node)
    vis[node]=True
    for e in mstGraph[node]:
        if vis[e.idx]==False:
            dfs(e.idx)
            travelRoute.append(node)

# Creates the travel route, which is a list of addresses chosen to minimize time and distance
def getTravelRoute(mst,n,addressList,num):
    distUpdate = []
    timeUpdate = []
    fromToUpdate = []
    for i in range(0,n):
        vis.append(False)
    global mstGraph
    mstGraph=mst
    dfs(0)
    print("TravelRoute-->",end=" ")
    for i in range(0,len(travelRoute)):
        print(travelRoute[i],end=' ')
    print()

    for i in range(1,len(travelRoute)):
        if num ==0:
            distUpdate.append(pickMatrix[travelRoute[i-1]][travelRoute[i]][1])
            timeUpdate.append(pickMatrix[travelRoute[i-1]][travelRoute[i]][0])
        elif num == 1:
            distUpdate.append(dropMatrix[travelRoute[i-1]][travelRoute[i]][1])
            timeUpdate.append(dropMatrix[travelRoute[i-1]][travelRoute[i]][0])
        fromToUpdate.append([addressList[travelRoute[i-1]],addressList[travelRoute[i]]])

    return [travelRoute,distUpdate,timeUpdate,fromToUpdate]

#Calculates the time and distance if the driver gave rides to clients one-by-one which is the slow way
def calculateSlowCost(length):
    totalDist =0
    totalTime = 0
    for i in range (1,length):
        totalDist+= pickMatrix[0][i][1]+pickDropDist[i][1]+dropMatrix[0][i][1]
        totalTime+= convertTime(pickMatrix[0][i][0])+convertTime(pickDropDist[i][0])+convertTime(dropMatrix[0][i][0])
    return [totalDist,totalTime]

#Used to convert strings of time to numbers, the strings are fetched from the Maps API  
def convertTime(time):
    n =0
    if "hour" not in time:
        return float(time[:-4])
    else:
        s = time[:-4].split()
        if s[0].isnumeric():
            n += float(s[0])*60
        if s[2].isnumeric():
            n+= float(s[2])
        return n









