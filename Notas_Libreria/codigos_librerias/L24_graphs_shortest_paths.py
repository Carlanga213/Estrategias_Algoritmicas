import random

from enum import Enum
from itertools import combinations
from functools import total_ordering


class NodeColor(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


@total_ordering
class Node:
    def __init__(self, value: int):
        self.value = value
        self.color = NodeColor.WHITE
        self.discovered = float("inf")
        self.finished = float("inf")
        self.d = float("inf")
        self.parent: Node = None

    def __repr__(self) -> str:
        return str(self.value)

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)


class GraphType(Enum):
    UNDIRECTED = 0
    DIRECTED = 1


class Graph:
    def __init__(self, type_: GraphType):
        self.type = type_
        self.V: dict[int, Node] = dict()
        self.E: dict[tuple[Node, Node], float] = dict()
        self.Adj: dict[Node, set[Node]] = dict()

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

    def __reset_nodes(self):
        for v in self.V.values():
            v.color = NodeColor.WHITE
            v.discovered = float("inf")
            v.finished = float("inf")
            v.d = float("inf")
            v.parent = None

    def w(self, u: Node, v: Node) -> float:
        if not isinstance(u, Node):
            u = self.get_node(u)
        if not isinstance(v, Node):
            v = self.get_node(v)
        # graph must be directed
        return self.E.get((u, v), None)

    def __relax(self, u: Node, v: Node) -> bool:
        # TODO
        pass

    def bellman_ford(self, s: int) -> bool:
        # TODO
        pass

    def dags(self, s: int):
        # TODO
        pass

    def dijkstra(self, s: int):
        assert all(
            [w >= 0 for w in self.E.values()]
        ), "All weights must be non-negative."
        # TODO
        pass

    def print_path(self, s: int, v: int) -> list[tuple[int, float]]:
        # TODO
        pass

    def bellman_ford_shortest_paths(self, s: Node, v: Node) -> list[tuple[int, float]]:
        if self.bellman_ford(s):
            return self.print_path(s, v)
        raise ValueError("Negative weight cycle found in Graph.")

    def dags_shortest_paths(self, s: Node, v: Node) -> list[tuple[int, float]]:
        self.dags(s)
        return self.print_path(s, v)

    def dijkstra_shortest_paths(self, s: Node, v: Node) -> list[tuple[int, float]]:
        self.dijkstra(s)
        return self.print_path(s, v)


if __name__ == "__main__":
    G = Graph(GraphType.DIRECTED)
    nodes = range(20)
    G.add_nodes(nodes)
    edges = [(i, j, random.random()) for i, j in combinations(nodes, 2)]
    random.shuffle(edges)
    edges = edges[:50]
    G.add_edges(edges)

    assert (
        G.bellman_ford_shortest_paths(0, 18)
        == G.dijkstra_shortest_paths(0, 18)
        == G.dags_shortest_paths(0, 18)
    )
