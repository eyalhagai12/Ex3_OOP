import numpy as np

class Edge:
    def __init__(self, src: int = 0, dst: int = 0, w: float = 0):
        self.src = src
        self.dst = dst
        self.weight = w

    def get_src(self):
        return self.src
    
    def get_dst(self):
        return self.dst

    def get_weight(self):
        return self.weight
