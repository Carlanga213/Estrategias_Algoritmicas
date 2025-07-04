import random

from enum import Enum
from itertools import combinations
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, value: int):
        self.value = value
        self.key = float("inf")  # prim (WEIGHT EN LAS DIAPOSITIVAS)
        self.parent: Node = None  # prim

    def __repr__(self) -> str:
        return str(self.value)

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)


class DisjointSets:
    def __init__(self):
        self.sets = []

    def make_set(self, x):
        self.sets.append({x})

    def find_set(self, x):
        for s in self.sets:
            if x in s:
                return s
        return None

    def union(self, x, y):
        s_x = self.find_set(x)
        s_y = self.find_set(y)
        if s_x and s_y and s_x != s_y:
            s_union = s_x.union(s_y)
            self.sets.remove(s_x)
            self.sets.remove(s_y)
            self.sets.append(s_union)


class GraphType(Enum):
    UNDIRECTED = 0
    DIRECTED = 1


class Graph:
    def __init__(self, type_: GraphType):
        self.type = type_
        self.V: dict[int, Node] = dict()
        self.E: dict[tuple[Node, Node], float] = dict()
        self.Adj: dict[Node, set[Node]] = dict()

    def w(self, u: Node, v: Node) -> float:
        if not isinstance(u, Node):
            u = self.get_node(u)
        if not isinstance(v, Node):
            v = self.get_node(v)
        return self.E.get((u, v), self.E.get((v, u), None))

    def __repr__(self):
        return str(self.Adj)

    def get_node(self, s: int) -> Node:
        return self.V.get(s, None)

    def add_node(self, v: int):
        v_node = self.get_node(v)
        if not v_node:
            v_node = Node(v)
            self.V[v] = v_node
            self.Adj[v_node] = set()

    def add_edge(self, u: int, v: int, w: float):
        u = self.get_node(u)
        v = self.get_node(v)
        if u and v:
            self.E[(u, v)] = w
            self.Adj[u].add(v)
            if self.type == GraphType.UNDIRECTED:
                self.Adj[v].add(u)
        else:
            raise ValueError("Node not found in graph")

    def add_nodes(self, v_list: list[int]):
        for v in v_list:
            self.add_node(v)

    def add_edges(self, e_list: list[tuple[int, int, float]]):
        for e in e_list:
            self.add_edge(*e)

    def kruskal(self) -> set[tuple[int, int, float]]:
        # TODO
        pass

    def prim(self, r: int) -> set[tuple[int, int, float]]:
        # TODO
        pass


if __name__ == "__main__":
    G = Graph(GraphType.UNDIRECTED)
    nodes = range(20)
    G.add_nodes(nodes)
    edges = [(i, j, random.random()) for i, j in combinations(nodes, 2)]
    random.shuffle(edges)
    edges = edges[:50]
    G.add_edges(edges)

    A_k = G.kruskal()
    A_p = G.prim(0)
    assert abs(sum([w for u, v, w in A_k]) - sum([w for u, v, w in A_p])) <= 0.001
