import unittest

from Node import Node
from Edge import Edge
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class NodeTestCase(unittest.TestCase):

    def test_get_id(self):
        node = Node()
        self.assertEqual(node.get_id(), -1)
        node.id = 4
        self.assertEqual(node.get_id(), 4)

    def test_add_in_edge(self):
        node = Node()
        self.assertEqual(node.get_in_edges(), {})
        node.add_in_edge(Edge(0, 5, node.get_id(), 3.314))
        self.assertNotEqual(node.get_in_edges(), {})
        self.assertTrue(len(node.get_in_edges()) == 1)

    def test_add_out_edge(self):
        node = Node()
        self.assertEqual(node.get_out_edges(), {})
        node.add_out_edge(Edge(0, node.get_id(), 5, 3.314))
        self.assertNotEqual(node.get_out_edges(), {})
        self.assertTrue(len(node.get_out_edges()) == 1)

    def test_remove_in_edge(self):
        node = Node()
        node.add_in_edge(Edge(0, 5, node.get_id(), 3.314))
        node.add_in_edge(Edge(1, 4, node.get_id(), 2.314))
        self.assertTrue(len(node.in_edges) == 2)
        self.assertEqual(node.remove_in_edge(5), True)
        self.assertTrue(len(node.in_edges) == 1)
        self.assertEqual(node.remove_in_edge(5), False)

    def test_remove_out_edge(self):
        node = Node()
        node.add_out_edge(Edge(0, node.get_id(), 5, 3.314))
        node.add_out_edge(Edge(1, node.get_id(), 4, 2.314))
        self.assertTrue(len(node.out_edges) == 2)
        self.assertEqual(node.remove_out_edge(5), True)
        self.assertTrue(len(node.out_edges) == 1)
        self.assertEqual(node.remove_out_edge(5), False)


class DiGraphTestCase(unittest.TestCase):

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        for n in range(4):
            graph.add_node(n)
        for n in range(1, 4):
            graph.add_edge(n, 0, 1)
        self.assertEqual(len(graph.all_in_edges_of_node(0)), 3)

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        for n in range(4):
            graph.add_node(n)
        for n in range(1, 4):
            graph.add_edge(0, n, 1)
        self.assertEqual(len(graph.all_out_edges_of_node(0)), 3)

    def test_add_edge(self):
        graph = DiGraph()
        for n in range(4):
            graph.add_node(n)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1.1)
        self.assertTrue(graph.e_size() == 2)
        self.assertTrue(len(graph.nodes[0].out_edges) == 1)
        self.assertTrue(len(graph.nodes[0].in_edges) == 1)
        self.assertTrue(len(graph.nodes[1].out_edges) == 1)
        self.assertTrue(len(graph.nodes[1].in_edges) == 1)

    def test_add_node(self):
        graph = DiGraph()
        self.assertTrue(graph.v_size() == 0)
        for n in range(4):
            graph.add_node(n)
        self.assertTrue(graph.v_size() == 4)

    def test_remove_node(self):
        graph = DiGraph()
        for n in range(2):
            graph.add_node(n)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1.1)
        graph.remove_node(0)
        self.assertTrue(graph.e_size() == 0)
        self.assertTrue(len(graph.nodes[1].out_edges) == 0)
        self.assertTrue(len(graph.nodes[1].in_edges) == 0)

    def test_remove_edge(self):
        graph = DiGraph()
        for n in range(4):
            graph.add_node(n)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1.1)
        graph.add_edge(1, 3, 1.9)
        self.assertTrue(graph.e_size() == 3)
        self.assertTrue(len(graph.nodes[1].get_out_edges()) == 2)
        graph.remove_edge(1, 3)
        self.assertTrue(graph.e_size() == 2)
        self.assertTrue(len(graph.nodes[1].get_out_edges()) == 1)


class GraphAlgoTestCase(unittest.TestCase):
    def test_load_from_json(self):
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("../data/A0.json")
        self.assertEqual(g_algo.__repr__(), "Graph: |V|=11 , |E|=22")
        self.assertEqual(g_algo.get_graph().get_all_v()[0].get_id(), 0)


if __name__ == '__main__':
    unittest.main()
