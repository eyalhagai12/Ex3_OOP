import copy
from GraphInterface import GraphInterface
from Node import Node
from Edge import Edge


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def v_size(self):
        return len(self.nodes)

    def e_size(self):
        return len(self.edges)

    def get_all_v(self):
        return self.nodes

    def get_node(self, _id: int):
        return self.nodes[_id]

    def __copy__(self):
        c = DiGraph()
        c.nodes = copy.deepcopy(self.nodes)
        c.edges = copy.deepcopy(self.edges)
        c.mc = copy.deepcopy(self.mc)
        return c

    def all_in_edges_of_node(self, id1: int):
        out = {}
        for edge in self.nodes[id1].get_in_edges().values():
            out[edge.get_src()] = edge.get_weight()
        return out

    def all_out_edges_of_node(self, id1: int):
        out = {}
        for edge in self.nodes[id1].get_out_edges().values():
            out[edge.get_dst()] = edge.get_weight()
        return out

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        if len(self.edges) == 0:
            e = Edge(0, id1, id2, weight)
            self.edges[0] = e
            self.nodes[id1].add_out_edge(e)
            self.nodes[id2].add_in_edge(e)
        else:
            _id = max(self.edges.keys()) + 1
            e = Edge(_id, id1, id2, weight)
            self.edges[_id] = e
            self.nodes[id1].add_out_edge(e)
            self.nodes[id2].add_in_edge(e)
        self.mc += 1

    def add_node(self, node_id: int, pos: tuple = None):
        if node_id in self.nodes.keys():
            return False
        else:
            self.nodes[node_id] = Node(node_id, pos)
            self.mc += 1
            return True

    def remove_node(self, node_id: int):
        if node_id not in self.nodes.keys():
            return False
        else:
            temp_in = self.nodes[node_id].get_in_edges()
            temp_out = self.nodes[node_id].get_out_edges()

            temp_in = [edge for edge in temp_in.values()]
            temp_out = [edge for edge in temp_out.values()]

            for edge in temp_in:
                self.remove_edge(edge.get_src(), edge.get_dst())
            for edge in temp_out:
                self.remove_edge(edge.get_src(), edge.get_dst())
            del self.nodes[node_id]
            self.mc += 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int):
        if node_id1 not in self.nodes.keys() or node_id2 not in self.nodes.keys():
            return False
        else:
            _id = self.nodes[node_id1].out_edges[node_id2].get_id()
            del self.edges[_id]

            self.nodes[node_id1].remove_out_edge(node_id2)
            self.nodes[node_id2].remove_in_edge(node_id1)

            self.mc += 1
            return True

    def __repr__(self):
        return f"Graph: |V|={len(self.nodes)} , |E|={len(self.edges)}"
