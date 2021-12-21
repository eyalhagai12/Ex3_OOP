import math

from FibHeap import FibonacciHeap
from Node import Node
from DiGraph import DiGraph


def infinity_weights(graph: DiGraph):
    for node in graph.get_all_v().values():
        node.set_weight(math.inf)


def reset_weights(graph: DiGraph):
    for node in graph.get_all_v().values():
        node.set_weight(0)


def reset_tags(graph: DiGraph):
    for node in graph.get_all_v().values():
        node.set_tag(0)


def dijkstra(graph: DiGraph, source: Node):
    heap = FibonacciHeap()
    infinity_weights(graph)
    source.set_weight(0)
    heap.insert_node(source)
    while heap.trees:
        temp = heap.extract_min()
        if temp.get_tag() == 1:
            continue
        temp_edges = temp.get_out_edges()
        for edge in temp_edges.values():
            weight = temp.get_weight() + edge.get_weight()
            if weight < graph.get_node(edge.get_dst()).get_weight():
                graph.get_node(edge.get_dst()).set_weight(weight)
        # temp.set_tag(1)
        for edge in temp_edges.values():
            if graph.get_node(edge.get_dst()).get_tag() != 1:
                heap.insert_node(value=graph.get_node(edge.get_dst()))

        temp.set_tag(1)
    reset_tags(graph)


def find_max_distance(graph: DiGraph, source: Node):
    dijkstra(graph, source)
    max_weight = -math.inf
    index = -1
    for node in graph.get_all_v().values():
        if node.get_weight() > max_weight:
            max_weight = node.get_weight()
            index = node.get_id()
    return index
