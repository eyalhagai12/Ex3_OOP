import json
import matplotlib.pyplot as plt
import warnings

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
            if "id" in n.keys() and "pos" in n.keys():
                position = n["pos"].split(",")
                idd = n["id"]
                graph_res.add_node(node_id=idd, pos=(float(position[0]), float(position[1])))
            else:
                if "id" in n.keys():
                    idd = n["id"]
                    graph_res.add_node(node_id=idd, pos=None)
                else:
                    graph_res.add_node(node_id=None, pos=None)
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

    def plot_graph(self) -> None:
        # if graph's node have no position, generate position for them
        handle_empty_graph(self.graph)
        fig = plt.figure()
        axes = fig.add_axes([0, 0, 1, 1])
        nodes = self.graph.get_all_v().values()
        x = []
        y = []
        x = [z.pos[0] for z in nodes]
        y = [-z.pos[1] for z in nodes]
        for node in nodes:
            axes.text(node.pos[0], node.pos[1], node.get_id(),
                      va='top',
                      ha='right',
                      color='blue',
                      fontsize=9,
                      bbox=dict(boxstyle='square, pad=0.2', ec='gray', fc='pink', alpha=0.65),
                      zorder=99)
            plt.annotate("",
                         xy=(node.pos[0], node.pos[1]),
                         xytext=(x, y),
                         arrowprops=dict(arrowstyle="->", color='black')
                         )
        plt.xticks([])
        plt.yticks([])
        plt.scatter(x, y, color='red')
        plt.show()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    def __repr__(self):
        return f"{self.graph}"


if __name__ == "__main__":
    g_algo = GraphAlgo(DiGraph())
    g_algo.load_from_json("../data/A1.json")
    print(g_algo.centerPoint())
