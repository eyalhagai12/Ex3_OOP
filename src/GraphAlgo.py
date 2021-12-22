import json
import numpy as np
import threading

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from Edge import Edge
from Utils import *


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = None):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        @returns the directed graph on which the algorithm works on.
        """
        return self.graph

    def save_to_json(self, file):
        """
        Saves the graph in JSON format to a file
        @param file: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        with open(file, "w") as f:
            json.dump(self, fp=f, indent=4, default=lambda x: x.__dict__)
        return True

    def load_from_json(self, file):
        """
        Loads a graph from a json file.
        @param file: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        graph_res = DiGraph()
        with open(file, "r") as f:
            _dict = json.load(f)
        for n in _dict["Nodes"]:
            position = n["pos"].split(",")
            idd = n["id"]
            graph_res.add_node(node_id=idd, pos=(position[0], position[1]))
        for edge in _dict["Edges"]:
            graph_res.add_edge(edge["src"], edge["dest"], edge["w"])
        self.graph = graph_res
        if self.graph is not None:
            return True
        else:
            return False

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        @returns The nodes id, min-maximum distance
        """
        max_nodes = []
        min_weight = math.inf
        index = -1
        for node in self.graph.get_all_v().values():
            reset_all(self.graph)
            node_id = find_max_distance(self.graph, node)
            temp = self.graph.get_node(node_id)
            max_nodes.append(temp)
            if min_weight > temp.get_weight():
                min_weight = temp.get_weight()
                index = node.get_id()

        return index, min_weight

    def shortest_path(self, source: int, destination: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param source: The start node id
        @param destination: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        """
        reset_all(self.graph)
        dijkstra(self.graph, self.graph.get_node(source))
        path = make_shortest_list(self.graph.get_node(destination))
        return self.graph.get_node(destination).get_weight(), path

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        @param node_lst: A list of nodes id's
        @returns A list of the nodes id's in the path, and the overall distance
        """
        return custom_search(self.graph, node_lst)

    def __repr__(self):
        return f"{self.graph}"


if __name__ == "__main__":
    g_algo = GraphAlgo(DiGraph())
    g_algo.load_from_json("../data/A1.json")
    print(g_algo.centerPoint())
