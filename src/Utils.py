import math
from collections import OrderedDict

# from FibHeap import FibonacciHeap
from heapq import heappush
from heapq import heappop
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


def reset_info(graph: DiGraph):
    for node in graph.get_all_v().values():
        node.set_info(None)


def reset_all(graph: DiGraph):
    for node in graph.get_all_v().values():
        node.set_weight(0)
        node.set_tag(0)
        node.set_info(None)


def dijkstra(graph: DiGraph, source: Node):
    heap = []
    infinity_weights(graph)
    source.set_weight(0)
    heappush(heap, source)
    while heap:
        temp = heappop(heap)
        if temp.get_tag() == 1:
            continue
        temp_edges = temp.get_out_edges()
        for edge in temp_edges.values():
            weight = temp.get_weight() + edge.get_weight()
            if weight < graph.get_node(edge.get_dst()).get_weight():
                graph.get_node(edge.get_dst()).set_weight(weight)
                next_node = graph.get_node(edge.get_dst())
                next_node.set_info(temp)  # for shortest path

        for edge in temp_edges.values():
            if graph.get_node(edge.get_dst()).get_tag() != 1:
                next_node = graph.get_node(edge.get_dst())
                heappush(heap, next_node)

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


def threaded_find_max_distance(graph: DiGraph, ids: list, weights: list):
    res = []
    for idd in ids:
        source = idd
        dijkstra(graph, source)
        max_weight = -math.inf
        index = -1
        for node in graph.get_all_v().values():
            if node.get_weight() > max_weight:
                max_weight = node.get_weight()
                index = node.get_id()
        res.append((index, graph.get_node(index).get_weight()))
    weights.extend(res)


def make_shortest_list(graph: DiGraph, destination: Node):
    x = []
    parent = destination.get_info()
    while parent is not None:
        x.insert(0, parent.get_id())
        parent = parent.get_info()
    if destination.get_weight() is not math.inf:
        x.append(destination.get_id())
    return x


def custom_search(graph: DiGraph, cities: list):
    result = []
    best_node = graph.get_node(cities[0])
    overall_distance = 0

    while best_node is not None:
        reset_all(graph)
        (n, d) = add_closest(graph, best_node, cities, result)
        best_node = n
        if d is not math.inf:
            overall_distance += d
    temp = result
    result = list(OrderedDict.fromkeys(result))
    return result, overall_distance


def add_closest(graph: DiGraph, src: Node, cities: list, result: list):
    dijkstra(graph, src)
    min_dist = math.inf
    best_node = None
    for index in cities:
        node = graph.get_node(index)
        if node is not None and node.get_id() is not src.get_id() and node.get_id() not in result:
            if node.get_weight() < min_dist:
                min_dist = node.get_weight()
                best_node = node

    if best_node is not None:
        path = make_shortest_list(graph, best_node)
        result.extend(path)

    return best_node, min_dist
