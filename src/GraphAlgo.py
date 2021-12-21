import json
import numpy as np

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from Edge import Edge
from Utils import *


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph):
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
        reset_all(self.graph)
        weights = []
        for node in self.graph.get_all_v().values():
            reset_weights(self.graph)
            node_id = find_max_distance(self.graph, node)
            weights.append((node_id, self.graph.get_node(node_id).get_weight()))
        arr = np.array(weights)[:, 1].astype(float)
        min_value = min(arr)
        index = [x[1] for x in weights].index(min_value)
        weight = weights[index][1]
        return index, weight

    def shortest_path(self, source: int, destination: int) -> (float, list):
        reset_all(self.graph)
        dijkstra(self.graph, self.graph.get_node(source))
        path = make_shortest_list(self.graph, self.graph.get_node(destination))
        return self.graph.get_node(destination).get_weight(), path

    def __repr__(self):
        return f"{self.graph}"


if __name__ == "__main__":
    g_algo = GraphAlgo(DiGraph())
    g_algo.load_from_json("../data/A1.json")
    print(g_algo.centerPoint())
