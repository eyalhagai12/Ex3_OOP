from GraphInterface import GraphInterface
from Node import Node
from Edge import Edge


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.mc = 0

    def v_size(self):
        return len(self.nodes)

    def e_size(self):
        return len(self.edges)

    def get_all_v(self):
        return self.nodes

    def all_in_edges_of_node(self, id1: int):
        out = {}
        for edge in self.nodes[id1].get_in_edges().values():
            out[edge.get_src()] = edge.get_weight()
        return out
        ###
        # out = {}
        # for edge in self.nodes[id1].get_in_edges():
        #     out[edge.get_src()] = edge.get_weight()
        # return out

    def all_out_edges_of_node(self, id1: int):
        out = {}
        for edge in self.nodes[id1].get_out_edges().values():
            out[edge.get_dst()] = edge.get_weight()
        return out
        ###
        # out = {}
        # for edge in self.nodes[id1].get_out_edges():
        #     out[edge.get_dst()] = edge.get_weight()
        # return out

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        self.nodes[id1].add_out_edge((id1, id2, weight))
        self.nodes[id2].add_in_edge((id1, id2, weight))
        self.edges.append(Edge(id1, id2, weight))
        self.mc += 1

    def add_node(self, node_id: int, pos: tuple = None):
        if node_id in self.nodes.keys():
            return False
        else:
            self.nodes[node_id] = Node((node_id, pos))
            self.mc += 1
            return True

    def remove_node(self, node_id: int):
        if node_id not in self.nodes.keys():
            return False
        else:
            # remove edges of node from self.edges
            to_remove = []
            for i, edge in enumerate(self.edges):
                if edge.get_src() == node_id or edge.get_dst() == node_id:
                    to_remove.append(self.edges[i])
            for edge in to_remove:
                self.edges.remove(edge)

            # remove edges of node from other nodes
            for node in self.nodes.values():
                if node.get_id() == node_id:
                    continue
                if node_id in node.in_edges.keys():
                    del node.in_edges[node_id]
                if node_id in node.out_edges.keys():
                    del node.out_edges[node_id]

            del self.nodes[node_id]
            self.mc += 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int):
        if node_id1 not in self.nodes.keys() or node_id2 not in self.nodes.keys():
            return False
        else:
            self.nodes[node_id1].remove_out_edge(node_id2)
            self.nodes[node_id2].remove_in_edge(node_id1)
            for i, edge in enumerate(self.edges):
                if edge.get_src() == node_id1 and edge.get_dst() == node_id2:
                    self.edges.remove(self.edges[i])
                    break
            self.mc += 1
            return True

    def __repr__(self):
        return f"Graph: |V|={len(self.nodes)} , |E|={len(self.edges)}"
