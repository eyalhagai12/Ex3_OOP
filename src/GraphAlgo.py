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
        return self.graph

    def save_to_json(self, file):
        with open(file, "w") as f:
            json.dump(self, fp=f, indent=4, default=lambda x: x.__dict__)

    def load_from_json(self, file):
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

    def centerPoint(self) -> (int, float):
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
        reset_all(self.graph)
        dijkstra(self.graph, self.graph.get_node(source))
        path = make_shortest_list(self.graph, self.graph.get_node(destination))
        return self.graph.get_node(destination).get_weight(), path

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        return custom_search(self.graph, node_lst)

    def __repr__(self):
        return f"{self.graph}"


if __name__ == "__main__":
    g_algo = GraphAlgo(DiGraph())
    g_algo.load_from_json("../data/A1.json")
    print(g_algo.centerPoint())
