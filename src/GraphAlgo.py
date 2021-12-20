import json

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from Edge import Edge


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph):
        self.graph = g

    def get_graph(self):
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
            graph_res.add_node(n["id"], pos=(position[0], position[1]))
        for edge in _dict["Edges"]:
            graph_res.nodes[edge["src"]].add_in_edge((edge["src"], edge["dest"], edge["w"]))
            graph_res.nodes[edge["dest"]].add_out_edge((edge["src"], edge["dest"], edge["w"]))
            graph_res.edges.append(Edge(edge["src"], edge["dest"], edge["w"]))
        self.graph = graph_res

    def __repr__(self):
        return f"{self.graph}"
