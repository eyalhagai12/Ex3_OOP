from Edge import Edge


class Node:
    def __init__(self, id: int = -1, pos: tuple = None):
        self.id = id
        self.in_edges = {}
        self.out_edges = {}
        self.pos = pos

        # for GraphAlgo
        self.weight = 0
        self.tag = 0
        #

    def get_id(self):
        return self.id

    def get_in_edges(self):
        return self.in_edges

    def get_out_edges(self):
        return self.out_edges

    def add_in_edge(self, e: tuple):
        self.in_edges[e[0]] = Edge(e[0], e[1], e[2])

    def add_out_edge(self, e: tuple):
        self.out_edges[e[1]] = Edge(e[0], e[1], e[2])

    def remove_out_edge(self, dst: int):
        if dst not in self.out_edges.keys():
            return False
        else:
            del self.out_edges[dst]
            return True

    def remove_in_edge(self, src: int):
        if src not in self.in_edges.keys():
            return False
        else:
            del self.in_edges[src]
            return True

    def __repr__(self):
        return f"{self.id}: |edges out| {len(self.out_edges)} |edges in| {len(self.in_edges)}"
