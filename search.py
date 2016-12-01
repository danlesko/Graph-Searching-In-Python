#!/usr/bin/python3

from __future__ import print_function
from collections import defaultdict
# Importing some common modules
import os, sys
import queue

# ------ You could use any python data structure or create your own class to maintain nodes, edges, queues etc. ----
# ------ This is just a simple skeleton. You don't have to use it. You can create your own code from scratch if you wish ---- 


# Helper functions
# I/O functions to read the different input files
# NOTE: The input files can simply be the filename if it is in the same directory as the program. 
# Otherwise you have to specify the full path
# You could use functions from the "os" module to navigate file paths

# This function should read an heuristics file. You could use a dictionary or use any other data structure of your choice
def read_heuristics_file(heuristics_file):
    # You should use open() to open the file and then use read() or readlines() to read it. Remove the "pass" statement and fill in your code
    heuristic_values = dict()
    with open(heuristics_file, "r") as f:
        for line in f:
            data = line.split(" ")
            heuristic_values[str(data[0])] = int(data[1])

    # print (heuristic_values)
    return heuristic_values

def createGraph(node_file, edge_file):
    
    #create graph
    graph = dict()

    #read in nodes, and neighbors w/ weights
    with open(edge_file, "r") as f:
        for line in f:
            data = line.split(" ")
            if data[0] in graph:
                temp = graph[data[0]]
                temp.update({str(data[1]) : int(data[2])})
                graph[data[0]] = temp
            else:
                graph[str(data[0])] = {str(data[1]) : int(data[2])}

    #if there is a node that does not have any neighbors, create it with an empty value
    with open(node_file, "r") as f:
        for line in f:
            data = line.strip('\n')
            # print (data)
            if data[0] not in graph:
                graph[data[0]] = {}
    print (graph)
    return graph

# Search functions
def breadth_first_search(graph, start_node, end_node):
    #this algorithm will return the first path to the end node
    
    #create and add start node to queue
    queue = []
    queue.append([start_node])

    #while there are still values in the queue
    while queue:

        #get the first path in queue
        path = queue.pop(0)
        #get first value in path
        vertex = path[-1]

        #if we are at the goal, return
        if vertex == end_node:
            return path

        #traverse graph in alphabetical order, adding the neighbors 
        for key, value in sorted(graph[vertex].items(), reverse=True):
            new_path = list(path)
            new_path.append(key)
            queue.append(new_path)

    return None

def depth_first_search(graph, start_node, end_node):

    #initilize stack with the start node, visitid as empty
    stack = [start_node]
    visited = []

    #while stack is not empty
    while stack:

        #get first value in stack
        vertex = stack.pop()

        while vertex not in visited:

            #if the vertex has no neighbors and it is not the end node, then we don't want it on our path
            if (not graph[vertex] and vertex != end_node):
                
                #grab a new vertex value from the stack
                vertex = stack.pop()
                if vertex == None:
                    break
                continue

            #add the vertex to visited nodes
            visited.append(vertex)

            if vertex in graph:
                #add neighbors of the current vertex to the stack
                for key, value in sorted(graph[vertex].items(), reverse=True):
                    stack.extend(key)
        
        #return visited, it is the path
        if end_node in visited:
            return visited 
            #
    return None

def uniform_cost_search(graph, start_node, end_node):

    #https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    def createPath(nodes, start, end):
        # print (nodes)
        path = []
        path.append(end)
        
        # print(end)

        recursePath(end, start, nodes, path)

        path.reverse()

        return path

    def recursePath(current, start, nodes, path):
        next = nodes[current]
        # print(next)
        path.append(next)
        if next != start:
            recursePath(next, start, nodes, path)
        return path


    dist = {}
    prev = {}

    Q = set(graph.keys())

    for vertex in graph:                # Initialization   
        dist[vertex] = sys.maxsize      # Unknown distance from source to v
        prev[vertex] = None             # Previous node in optimal path from source

    dist[start_node] = 0                # Distance from source to source

    while len(Q) > 0:                   # Source node will be selected first

        shortest = None
        u = ''

        # find closest node u
        for temp in Q:
            if shortest == None:
                shortest = dist[temp]
                u = temp
            elif (dist[temp] < shortest):
                shortest = dist[temp]
                u = temp

        # if we are at the end, create the path and return it
        if u == end_node:
            return createPath(prev, start_node, end_node)

        Q.remove(u)


        for neighbor, edge_weight in sorted(graph[u].items(), reverse=True):
            # print (dist[neighbor])
            alt = dist[u] + edge_weight
            if neighbor not in dist:
                continue
            elif alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u   

def greedy_search(graph, start_node, end_node, heuristic_values):

    # create priority queue and put heuristic value of start as well as path to start in the q
    q = queue.PriorityQueue()
    q.put( (heuristic_values[start_node], [start_node]) )

    # while the queue is not empty
    while q:

        # get path cost, and the path
        (path_cost, path) = q.get()

        #get last item in path
        path_end = path[-1]


        if path_end == end_node:
            return path

        # get neighbors, add path to neighbor to the path, then add that path to the q
        for neighbor, edge_weight in sorted(graph[path_end].items(), reverse=True):
            path_with_neighbor = list(path)
            path_with_neighbor.append(neighbor)
            q.put( (heuristic_values[neighbor], path_with_neighbor) )

    return None

def astar_search(graph, start_node, end_node, heuristic_values):

    #  https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode

    def heuristic_cost_estimate(start, goal):
        return abs(heuristic_values[start] - heuristic_values[goal])

    # the node in openSet having the lowest fScore[] value
    def get_current():
        pq = queue.PriorityQueue()
        for node in openSet:
            pq.put( (fScore[node], node) )

        return pq.get()[1]

    def reconstruct_path(cameFrom, current):
        total_path = [current]
        # for key, value in cameFrom.items():
        #     total_path.append(value)
        while current in cameFrom:
            current = cameFrom[current]
            total_path.append(current)
        total_path.reverse()
        return total_path

    # the set of nodes already evaluated.
    closedSet = set()

    # The set of currently discovered nodes still to be evaluated.
    # Initially, only the start node is known.
    openSet = set()
    openSet.add(start_node)

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    cameFrom = {}

    # For each node, the cost of getting from the start node to that node.
    gScore = {}
    gScore.setdefault(lambda: sys.maxsize) # map with default value of Infinity

    # The cost of going from start to start is zero.
    gScore[start_node] = 0

    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    fScore = {}
    fScore.setdefault(lambda: sys.maxsize) # map with default value of Infinity

    # For the first node, that value is completely heuristic.
    fScore[start_node] = heuristic_cost_estimate(start_node, end_node)

    while openSet:
        # print("openSet:\t" + str(openSet))
        # print("closedSet:\t" + str(closedSet))
        # print("cameFrom:\t" + str(cameFrom))

        current = get_current()
        if current == end_node:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.add(current)

        # iterate neighbors of current node
        for neighbor, edge_weight in sorted(graph[current].items(), reverse=True):
            if neighbor in closedSet:
                continue # Ignore the neighbor which is already evaluated.
            # The distance from start to a neighbor
            tentative_gScore = gScore[current] + edge_weight
            if neighbor not in openSet: # Discover a new node
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue # this is not a better path

            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor, end_node)

    return None

def pathCost(path):
    cost = 0;
    for i in range(0, len(path)):
        if (path[i] in graph and i != (len(path) -1) ):
            # print (graph[path[i]][path[i+1]])
            cost += graph[path[i]][path[i+1]]
    return cost

def writeToFile(path, cost, output_file):
    output = open(output_file, 'w')

    for i in range(0, len(path)):
        output.write(path[i])
        output.write("\n")

    output.write(str(cost))

    output.close()

# This is the main function that acts as an entry point to your program
if __name__=="__main__":
    # Simple welcome message
    print("Welcome to this uber cool search program..")

    # Check to see if there are the right number of arguments
    if len(sys.argv) != 8:
        print("Oops! Incorrect syntax..Lets try it again\npython search.py <algorithm_name> <node_file> <edge_file> <heuristics_file> <start_node> <end_node> <output_file>")
        exit(0)
        
    # Just for convenience, put all the values into variables
    algorithm = sys.argv[1]
    node_file = sys.argv[2]
    edge_file = sys.argv[3]
    heuristics_file = sys.argv[4]
    start_node = sys.argv[5]
    end_node = sys.argv[6]
    output_file = sys.argv[7]
    
    # Read the graph
    graph = createGraph(node_file, edge_file)
    heuristic_values = read_heuristics_file(heuristics_file)

    # Open a file to write the output contents. Use the write() function to write strings into it
    output = open(output_file, 'w')
    
    # Depending on the algorithm specified, call the corresponding function
    # Note that the heuristics file isn't used for uninformed search algorithms like BFS, DFS and UCS
    
    # Replace the "pass" statements with the corresponding function calls
    if algorithm == "breadth":
        path = breadth_first_search(graph, start_node, end_node)

    elif algorithm == "depth":
        path = depth_first_search(graph, start_node, end_node)

    elif algorithm == "uniform":
        path = uniform_cost_search(graph, start_node, end_node)

    elif algorithm == "greedy":
        path = greedy_search(graph, start_node, end_node, heuristic_values)

    elif algorithm == "astar":
        path = astar_search(graph, start_node, end_node, heuristic_values)

    else:
        print("Invalid algorithm identifier '%s'"%algorithm)
        exit(0)
    
    print (path)

    cost = pathCost(path)

    # print (cost)

    # Check if a valid path was returned. If it was, write the path contents and compute the cost of the path
    if not path:
        output.write("false")
    else:
        # Write the path to file.
        # If the path is a list of nodes, you can use the "join" operator. 
        # The output file must have a node each line and have the path cost in the last line
        
        writeToFile(path, cost, output_file)
        pass
    
    
    
    
    
    
    
    
    
    
