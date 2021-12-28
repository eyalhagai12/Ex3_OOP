# Ex3_OOP

This is our project on graph algorithms (specificly directed weighted graphs) and GUI in Python. It can be used to run
different algorithms using the plot_graph command. It can also be used on graphs using a simple Graphical User
Interface.

## Description

This is our project for implementing graph algorithms on directed weighted graphs and presenting them with mathplotlib
and / or GUI in Python. Our application can parse json files into graphs on which they can do different operations and
modifications to the graph.

Our project support commonly used graph algorithms such as: TSP (a simplified variation of TSP), center (finding the
center of the graph), Shortest Path (find the shortest path between two vertices)
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

1. clone his directory or download it
2. open the terminal in the directory of "Ex3_OOP"
3. run the command "pip install -r requirements.txt"
   and wait for installation to be done
4. type "cd src" in the command line
5. make sure that the json file you want to run is in the "data" directory and then to run the program use "python
   main.py <json_file_with_extension>"
   (example "python main.py A1.json")

* for this to run you must have python and pip installed

# Technologies

* Python 3.9
* Python's json, multiprocessing, Manager
* PyGame

# Functionalities

Our project supports algorithms on graphs that are weighted and directed, hence all algorithms mainly work on these
types of graphs.

### Main Algorithms

* **tsp**: this algorithm isn't exactly tsp but a variation of it that finds the shortest route between a subset
  vertices. the algorithm we used is not that fast but its does find a path (if it exists) in a reasonable time.
* **shortest path**: this algorithm is used to find the route with the lowest sum of weights (shortest path) between two
  verices. it's very similar to the bellman-ford algorithm, but it also keeps track of the route that we went through to
  reach the destination node and how much did it "cost" (or what is the distance from te source node to the destination
  node).
* **center**: This algorithm finds the center of the graph (if it exists, meaning if the graph is strongly connected).
  the center of a graph is the vertex that the distance from it to the farthest vertex from it is minimal. this
  algorithm uses djikstra's algorithm to find the farthest vertex from a given vertex.

### how to use them

* **tsp**: to use the tsp in the GUI, simply press the "tsp" button, tehn press on the nodes that you want the route to
  go through, when done press Enter and the route will be highlighted in green
* **shortest path**: to use the shortest path algorithm in hte GUI, press on the "shortest path" button and then choose
  the two nodes (source and destination in that order)
* **center**: to use center in the GUI, press on the "center" button and the center of the graph will be highlighted in
  green

### Graph Modifications

you can also add and remove vertices and edges simply with the GUI

* **add node**: to add a node, press on the "add node" button and then press where you want to add it on the screen
* **remove node**: to remove a node, press on the "remove node" button then press on the node you want to delete
* **add edge**: to add an edge, press on the "add edge" button, then choose two nodes (source and destination in that
  order)
  then a window will pop up asking you to assign a weight to that edge, put a weight in and press "add edge" in that
  window
* **remove edge**: to remove an edge, press on the "remove edge" button and the press on two connected nodes (source and
  destination of the edge in that order)

### Saving and Loading Graphs

* **saving**: to save a graph, press on the the save button and then go to the directory in which you want to save the graph file in, then give it a name (with json extension) and press save.
* **loading**: to load a graph, press on the load button, then search for the wanted file in the file manager and then choose it and pess open.

# Sources

* **Dijkstra's algorithm**: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

# Runtimes

The graphs that were tested in this test case are:

* G1.json
* G2.json
* G3.json
* 1,000Nodes.json (custom graph, could not upload to this repo because it was too big)
* 10,000Nodes.json (custom graph, could not upload to this repo because it was too big)

All graphs were tested at once. Runtime results are for the given graphs in the same order  
Each test was executed immediately after the previous test was done.  
**Results:**
<p align="center">
<img src="https://user-images.githubusercontent.com/77681248/147388322-cf95fa0e-8a7a-45f7-a617-a1b916d87924.png">
</p>
