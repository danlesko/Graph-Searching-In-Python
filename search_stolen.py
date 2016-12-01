#!/usr/bin/python3

from __future__ import print_function
# Importing some common modules
import os, sys

# ------ You could use any python data structure or create your own class to maintain nodes, edges, queues etc. ----
# ------ This is just a simple skeleton. You don't have to use it. You can create your own code from scratch if you wish ---- 


# Helper functions
# I/O functions to read the different input files
# NOTE: The input files can simply be the filename if it is in the same directory as the program. 
# Otherwise you have to specify the full path
# You could use functions from the "os" module to navigate file paths

# This function should read a node file. You could return a list or use any other data structure of your choice
def read_node_file(node_file):
    # You should use open() to open the file and then use read() or readlines() to read it. Remove the "pass" statement and fill in your code
    nodes = open(node_file).read().splitlines()
    # print (nodes)
    return nodes

# This function should read an edge file. You could use a dictionary or use any other data structure of your choice
def read_edge_file(edge_file):
    # You should use open() to open the file and then use read() or readlines() to read it. Remove the "pass" statement and fill in your code
    edges = open(edge_file).read().splitlines()
    # print (edges)
    return edges

# This function should read an heuristics file. You could use a dictionary or use any other data structure of your choice
def read_heuristics_file(heuristics_file):
    # You should use open() to open the file and then use read() or readlines() to read it. Remove the "pass" statement and fill in your code
    pass

# Search functions
def breadth_first_search(nodes, edges, start_node, end_node):
    pass

def dfs(graph, end, stack):
    while stack:
        currentNode = {}
        start, visited = stack.pop()
        if start in graph:
            currentNode = graph[start]
            del graph[start]
        
        if(start == end):
            return visited
        else:
            for key, value in sorted(currentNode.items(), reverse=True):
                stack.append((str(key), visited + [key]))

    return list()

   

def uniform_cost_search(nodes, edges, start_node, end_node):
    pass

def greedy_search(nodes, edges, start_node, end_node, heuristic_values):
    pass

def astar_search(nodes, edges, start_node, end_node, heuristic_values):
    pass

def createGraph(fileName):
    graph = dict()
    with open(fileName, "r") as f:
        for line in f:
            data = line.split(" ")
            if data[0] in graph:
                temp = graph[data[0]]
                temp.update({str(data[1]) : int(data[2])})
                graph[data[0]] = temp
            else:
                graph[str(data[0])] = {str(data[1]) : int(data[2])}
    return graph

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
    nodes = read_node_file(node_file) 
    edges = read_edge_file(edge_file)

    graph = createGraph(edge_file)
    print (graph)

    heuristic_values = read_heuristics_file(heuristics_file)
    # Open a file to write the output contents. Use the write() function to write strings into it
    output = open(output_file, 'w')
    
    # Depending on the algorithm specified, call the corresponding function
    # Note that the heuristics file isn't used for uninformed search algorithms like BFS, DFS and UCS
    
    # Replace the "pass" statements with the corresponding function calls
    if algorithm == "breadth":
        path = breadth_first_search(nodes, edges, start_node, end_node)
    elif algorithm == "depth":
        stack = [(start_node, list(start_node))]
        print (stack)
        path = dfs(graph, end_node, stack)

    elif algorithm == "uniform":
        path = uniform_cost_search(nodes, edges, start_node, end_node)
    elif algorithm == "greedy":
        path = greedy_search(nodes, edges, start_node, end_node, heuristic_values)
    elif algorithm == "astar":
        path = astar_search(nodes, edges, start_node, end_node, heuristic_values)
    else:
        print("Invalid algorithm identifier '%s'"%algorithm)
        exit(0)
    
    print (path)
    # Check if a valid path was returned. If it was, write the path contents and compute the cost of the path
    if not path:
        output.write("false")
    else:
        # Write the path to file.
        # If the path is a list of nodes, you can use the "join" operator. 
        # The output file must have a node each line and have the path cost in the last line
        pass
    
    
    
    
    
    
    
    
    
    