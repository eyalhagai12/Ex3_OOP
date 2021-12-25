# Ex3_OOP

This is our project on graph algorithms (specificly directed weighted graphs) and GUI in Python. It can be used to run
different algorithms using the plot_graph command. It can also be used on graphs using a simple Graphical User Interface.

## Description

This is our project for implementing graph algorithms on directed weighted graphs and presenting them with mathplotlib and / or GUI in Python.
Our application can parse json files into graphs on which they can do different operations and modifications to the graph.

Our project support commonly used graph algorithms such as: TSP (a simplified variation of TSP), 
center (finding the center of the graph), Shortest Path (find the shortest path between two vertices)
and Shortest Path Distance (find the distance between two nodes)

it also supports saving and loading graphs from and to json files
(Note: The json file structure should look like those in the data folder when trying to load them)

## Table of contents

1. [Getting started](#Getting-started)
2. [technologies](#Technologies)
3. [functionalities](#Functionalities)
4. [sources](#Sources)
5. [runtimes](#Runtimes)

# Getting started

FILL

# Technologies

* Python 3.9
* Python's json, multiprocessing, Manager

# Functionalities

Our project supports algorithms on graphs that are weighted and directed, hence all algorithms mainly work on these
types of graphs.

### Main Algorithms

* **tsp**: this algorithm isn't exactly tsp but a variation of it that finds the shortest route between a subset
  vertices. the algorithm we used is not that fast but its does find a path (if it exists) in a reasonable time.
* **shortestPath**: this algorithm is used to find the route with the lowest sum of weights (shortest path) between two
  verices. it's very similar to the bellman-ford algorithm, but it also keeps track of the route that we went through to
  reach the destination node and how much did it "cost" (or what is the distance from te source node to the destination
  node).
* **shortestPathDist**: This algorithm is used to find the distance between two vertices. This algorithm uses the
  shortestPath algorithm and just returns the length of the route (the sum of the weights in the route).
* **isConnected**: This function is used to check if the given graph is strongly connected. meaning that every vertex on
  this graph can reach any other vertex in the graph (in other words, there is a path between every two vertices in the
  graph). ths function uses topological sort to see if there is a vertex that all nodes can reach and that it can reach
  all nodes.
* **center**: This algorithm finds the center of the graph (if it exists, meaning if the graph is strongly connected).
  the center of a graph is the vertex that the distance from it to the farthest vertex from it is minimal. this
  algorithm uses djikstra's algorithm to find the farthest vertex from a given vertex.
  
### Graph Modifications

you can also add and remove vertices and edges simply with the GUI

* **add node**: In the GUI, go to Edit -> add node, and press on the screen where you want to add that new node.
* **remove node**: In the GUI, go to Edit -> remove node, and type the id of that node (the node's id is the blue number
  that appears above it).
* **add edge**: In the GUI, go to Edit -> add edge, and type "src,dest,weight" ("src" and "dest" are id's of the nodes
  and weight is the weight of the graph).
* **remove edge**: In the GUI, go to Edit -> remove node, and type "src,dest"

### Saving and Loading Graphs

* **saving**: To save a file go to File -> Save, then choose where to save your graph (graphs are saved in json format)
* **loading**: To load a graph go to File -> load, then go to the directory of that json file and choose the wanted file


   
   
   
   
   
