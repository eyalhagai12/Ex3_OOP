import math
import unittest
import time
import os

from os.path import exists
from Node import Node
from Edge import Edge
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Utils import gen_loc


class GraphAlgoTestCase(unittest.TestCase):

    def test_save_to_json(self):
        start = time.time()
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("../data_test/G1.json")
        g_algo.save_to_json("../data_test/G1_py.json")
        g_algo.load_from_json("../data_test/G2.json")
        g_algo.save_to_json("../data_test/G2_py.json")
        g_algo.load_from_json("../data_test/G3.json")
        g_algo.save_to_json("../data_test/G3_py.json")

        # g_algo.load_from_json("../data_test/1000Nodes.json")
        # g_algo.save_to_json("../data_test/1000_py.json")
        # g_algo.load_from_json("../data_test/10000Nodes.json")
        # g_algo.save_to_json("../data_test/10000_py.json")

        self.assertTrue(True)
        print("save ", "{:.3f}".format(time.time() - start), "s")

    def test_load_from_json(self):
        start = time.time()
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("../data_test/G1.json")
        g_algo.load_from_json("../data_test/G2.json")
        g_algo.load_from_json("../data_test/G3.json")

        # g_algo.load_from_json("../data_test/1000Nodes.json")
        # g_algo.load_from_json("../data_test/10000Nodes.json")

        self.assertTrue(True)
        print("load ", "{:.3f}".format(time.time() - start), "s")

    def test_shortest_path(self):
        start = time.time()
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("../data_test/G3.json")
        self.assertNotEqual(g_algo.shortest_path(0, 4), None)
        print("shortest path ", "{:.3f}".format(time.time() - start), "s")

    def test_tsp(self):
        start = time.time()
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("../data_test/G2.json")
        self.assertNotEqual(g_algo.TSP([0, 10, 12, 15, 26]), (math.inf, []))
        g_algo.load_from_json("../data_test/G3.json")
        self.assertNotEqual(g_algo.TSP([0, 10, 12, 15, 26]), (math.inf, []))
        print("tsp ", "{:.3f}".format(time.time() - start), "s")

    def test_centerPoint(self):
        start = time.time()
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("../data_test/G1.json")
        self.assertEqual(g_algo.centerPoint()[0], 8)
        g_algo.load_from_json("../data_test/G2.json")
        self.assertEqual(g_algo.centerPoint()[0], 0)
        g_algo.load_from_json("../data_test/G3.json")
        self.assertEqual(g_algo.centerPoint()[0], 40)

        # g_algo.load_from_json("../data_test/1000Nodes.json")
        # self.assertEqual(g_algo.centerPoint()[0], 362)
        # g_algo.load_from_json("../data_test/10000Nodes.json")
        # self.assertEqual(g_algo.centerPoint()[0], 3846)

        print("center ", "{:.3f}".format(time.time() - start), "s")


if __name__ == '__main__':
    unittest.main()
