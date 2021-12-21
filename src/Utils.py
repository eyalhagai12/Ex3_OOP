import math

from FibHeap import FibonacciHeap
from Node import Node
from DiGraph import DiGraph

if __name__ == '__main__':
    f = FibonacciHeap()
    n1 = Node(0, (1, 1))
    n1.set_weight(15)
    n2 = Node(1, (2, 2))
    n2.set_weight(2)
    n3 = Node(2, (3, 3))
    n3.set_weight(4)
    n4 = Node(3, (4, 4))
    n4.set_weight(7)
    f.insert(n1.get_weight(), value=n1)
    f.insert(n2.get_weight(), vauen2)
    f.insert(n3.get_weight(), n3)
    f.insert(n4.get_weight(), n4)


def infinity_weights(graph: DiGraph):
    for node in graph.get_all_v().values():
        node.set_weight(math.inf)


def reset_weights(graph: DiGraph):
    for node in graph.get_all_v():
        node.set_weight(0)


def dijkstra(graph: DiGraph, source: Node):
    heap = FibonacciHeap()
    infinity_weights(graph)
    source.set_weight(0)
    heap.insert(source.get_weight(), source)
    while heap.total_nodes > 0:
        temp = heap.extract_min().value
        if temp.get_tag() == 1:
            continue
        temp_edges = temp.get_out_edges()
        for edge in temp_edges.values():
            weight = temp.get_weight() + edge.get_weight()
            if weight < graph.get_node(edge.get_dst()).get_weight():
                graph.get_node(edge.get_dst()).set_weight(weight)
        temp.set_tag(1)
        for edge in temp_edges.values():
            if graph.get_node(edge.get_dst()).get_tag() != 1:
                heap.insert(graph.get_node(edge.get_dst()).get_weight(), graph.get_node(edge.get_dst()))


def find_max_distance(graph: DiGraph, source: Node):
    dijkstra(graph, source)
    max_weight = -math.inf
    index = -1
    for node in graph.get_all_v().values():
        if node.get_weight() > max_weight:
            max_weight = node.get_weight()
            index = node.get_id()
    return index
