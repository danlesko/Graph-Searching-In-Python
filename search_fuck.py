#!/usr/bin/python3

from __future__ import print_function
from collections import defaultdict


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

def create_graph(g, nodes, edges):
    for node in nodes:
        g.add_node(node)

    for edge in edges:
        parsedEdge = edge.split()
        g.add_edge(parsedEdge[0], parsedEdge[1], parsedEdge[2])


# This function should read an heuristics file. You could use a dictionary or use any other data structure of your choice
def read_heuristics_file(heuristics_file):
    # You should use open() to open the file and then use read() or readlines() to read it. Remove the "pass" statement and fill in your code
    pass

# Search functions
def breadth_first_search(g, start_node, end_node):
    # print (g.vert_dict[start_node])


   pass
    

def depth_first_search(g, start_node, end_node):
    # stack = [start_node]
    # visited = set()
    # while stack:
    #     vertex = stack.pop()
    #     while vertex not in visited:
    #         visited.add(vertex)
    #         stack.extend(g.edges[vertex])
    #         for v in visited:
    #             value = v
    #             if value in stack:
    #                 stack.remove(value)
    #     print (vertex)
    #     print (stack)
    #     print (visited)
    # return visited



    



    # print (g.edges['A'])
    #print (g.vert_dict[start_node])
    
    pass 

def uniform_cost_search(nodes, edges, start_node, end_node):
    pass

def greedy_search(nodes, edges, start_node, end_node, heuristic_values):
    pass

def astar_search(nodes, edges, start_node, end_node, heuristic_values):
    pass

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    

# This is the main function that acts as an entry point to your program
if __name__=="__main__":
    # Simple welcome message
    print("Welcome to this uber cool search program..")

    # Check to see if there are the right number of arguments
    if len(sys.argv) != 8:
        print("Oops! Incorrect syntax..Lets try it again\npython search.py <algorithm_name> <node_file> <edge_file> <heuristics_file> <start_node> <end_node> <output_file>")
        exit(0)
        
    # Just for convenience, put all the values into variables
    g = Graph()
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
    graph = create_graph(g, nodes, edges)

    print (g.edges)    

    heuristic_values = read_heuristics_file(heuristics_file)
    # Open a file to write the output contents. Use the write() function to write strings into it
    output = open(output_file, 'w')
    
    # Depending on the algorithm specified, call the corresponding function
    # Note that the heuristics file isn't used for uninformed search algorithms like BFS, DFS and UCS
    
    # Replace the "pass" statements with the corresponding function calls
    if algorithm == "breadth":
        path = breadth_first_search(g, start_node, end_node)
    elif algorithm == "depth":
        path = depth_first_search(g, start_node, end_node)
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
    
    
    
    
    
    
    
    
    
    