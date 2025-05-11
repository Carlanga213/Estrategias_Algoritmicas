from enum import Enum
from typing_extensions import Self
from typing import TypeVar

T = TypeVar("T")


class Color(Enum):
    RED = 0
    BLACK = 1


class Node:
    def __init__(
        self, key: T, color: Color = Color.RED, parent=None, left=None, right=None
    ) -> None:
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right
        self.key: T = key
        self.color: Color = color

    # DFS
    def __repr__(self, nil: Self, level=0):
        # Define the indentation for each level
        indent = "    " * level
        repr_str = f"{indent}Node(k={self.key}, c={self.color}, bh={self.bh(nil)})"
        # Recursively traverse the left and right subtrees
        if self.left != nil:
            repr_str += f"\n{self.left.__repr__(nil, level + 1)}"
        if self.right != nil:
            repr_str += f"\n{self.right.__repr__(nil, level + 1)}"
        return repr_str

    def bh(self, nil: Self) -> int:  # black height
        if self == nil:
            return 1
        bh = max(self.left.bh(nil), self.right.bh(nil)) + (
            1 if self.color == Color.BLACK else 0
        )
        return bh


class RBT:  # (Red Black Tree)
    def __init__(self) -> None:
        self.nil = Node(None, Color.BLACK)  # hojas nulas
        self.root = self.nil

    def __repr__(self) -> str:
        if self.root == self.nil:
            return str(None)
        return self.root.__repr__(self.nil, level=0)

    def assert_bst_property(self) -> bool:
        if self.root == self.nil:
            return True
        return self.__assert_bst_property(self.root)

    def __assert_bst_property(self, x: Node) -> bool:
        if x.left != self.nil and x.right != self.nil:
            return (
                x.left.key <= x.key
                and x.right.key >= x.key
                and self.__assert_bst_property(x.left)
                and self.__assert_bst_property(x.right)
            )
        if x.left != self.nil:
            return x.left.key <= x.key and self.__assert_bst_property(x.left)
        if x.right != self.nil:
            return x.right.key >= x.key and self.__assert_bst_property(x.right)
        return True

    def assert_rbt_property(self) -> bool:
        if self.root == self.nil:
            return True
        return self.root.color == Color.BLACK and self.__assert_rbt_property(self.root)

    def __assert_rbt_property(self, x: Node) -> bool:
        if x == self.nil:
            return x.color == Color.BLACK
        c1 = (
            x.left.color == Color.BLACK and x.right.color == Color.BLACK
            if x.color == Color.RED
            else True
        )  # propiedad roja
        c2 = x.left.bh(self.nil) == x.right.bh(self.nil)  # propiedad negra
        return (
            c1
            and c2
            and self.__assert_rbt_property(x.left)
            and self.__assert_rbt_property(x.right)
        )

    def in_order_walk(self) -> list[T]:
        return self.__in_order_walk(self.root)

    def __in_order_walk(self, x: Node) -> list[T]:
        if x != self.nil:
            return (
                self.__in_order_walk(x.left) + [x.key] + self.__in_order_walk(x.right)
            )
        return []

    def search(self, k: T) -> bool:
        return self.__search(self.root, k) != self.nil

    def __search(self, x: Node, k: T) -> Node:
        while x != self.nil and k != x.key:
            x = x.left if k < x.key else x.right
        return x

    def minimum(self) -> T:
        return self.__minimum(self.root).key

    def __minimum(self, x: Node) -> Node:
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self) -> T:
        return self.__maximum(self.root).key

    def __maximum(self, x: Node) -> Node:
        while x.right != self.nil:
            x = x.right
        return x

    def successor(self, k: T) -> T:
        x = self.__search(self.root, k)
        if x == self.nil:
            raise ValueError("Key not found")
        s = self.__successor(x)
        return s.key if s != self.nil else None

    def __successor(self, x: Node) -> Node:
        if x.right != self.nil:
            return self.__minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, k: T) -> T:
        x = self.__search(self.root, k)
        if x == self.nil:
            raise ValueError("Key not found")
        p = self.__predecessor(x)
        return p.key if p != self.nil else None

    def __predecessor(self, x: Node) -> Node:
        if x.left != self.nil:
            return self.__maximum(x.left)
        y = x.parent
        while y != self.nil and x == y.left:
            x = y
            y = y.parent
        return y

    def insert(self, k: T) -> bool:
        if self.search(k):
            return False
        self.__insert(Node(k, Color.RED))
        return True

    def __insert(self, z: Node) -> None:
        # TODO
        self.__insert_fixup(z)

    def __insert_fixup(self, z: Node):
        while z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:  # z's parent is a left child
                # TODO
                pass
            else:  # z's parent is a right child
                # TODO
                pass
        self.root.color = Color.BLACK

    def delete(self, k: T) -> bool:
        z = self.__search(self.root, k)
        if z != self.nil:
            self.__delete(z)
            return True
        return False

    def __delete(self, z: Node) -> None:
        y = z
        y_original_color = y.color
        if z.left == self.nil:  # sin hijos o un hijo derecho
            # TODO
            pass
        elif z.right == self.nil:  # un hijo izquierdo
            # TODO
            pass
        else:  # dos hijos
            # TODO
            pass
        if y_original_color == Color.BLACK:
            self.__delete_fixup(x)
        del z

    def __delete_fixup(self, x: Node):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    # TODO
                    pass
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    # TODO
                    pass
                else:
                    # TODO
                    pass
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    # TODO
                    pass
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    # TODO
                    pass
                else:
                    # TODO
                    pass
        x.color = Color.BLACK

    def __transplant(self, u: Node, v: Node) -> None:
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __left_rotate(self, x: Node) -> Node:
        if x.right == self.nil:
            raise Exception("Cannot left rotate")
        # TODO
        pass

    def __right_rotate(self, y: Node) -> Node:
        if y.left == self.nil:
            raise Exception("Cannot right rotate")
        # TODO
        pass


if __name__ == "__main__":

    t = RBT()
    for i in [9, 5, 1, 0, 6, 3, 2, 4, 7, 8]:
        t.insert(i)
    print(t)
    # Node(k=5, c=Color.BLACK, bh=3)
    #     Node(k=1, c=Color.RED, bh=2)
    #         Node(k=0, c=Color.BLACK, bh=2)
    #         Node(k=3, c=Color.BLACK, bh=2)
    #             Node(k=2, c=Color.RED, bh=1)
    #             Node(k=4, c=Color.RED, bh=1)
    #     Node(k=7, c=Color.RED, bh=2)
    #         Node(k=6, c=Color.BLACK, bh=2)
    #         Node(k=9, c=Color.BLACK, bh=2)
    #             Node(k=8, c=Color.RED, bh=1)
    print(t.in_order_walk())
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(t.assert_bst_property())
    # True
    print(t.search(10), t.search(9))
    # False, True
    print(t.minimum(), t.maximum())
    # 0, 9
    print(t.predecessor(5), t.successor(5))
    # 4, 6
    print(t.insert(10), t.assert_bst_property())
    # True, True
    print(t)
    # Node(k=5, c=Color.BLACK, bh=3)
    #     Node(k=1, c=Color.RED, bh=2)
    #         Node(k=0, c=Color.BLACK, bh=2)
    #         Node(k=3, c=Color.BLACK, bh=2)
    #             Node(k=2, c=Color.RED, bh=1)
    #             Node(k=4, c=Color.RED, bh=1)
    #     Node(k=7, c=Color.RED, bh=2)
    #         Node(k=6, c=Color.BLACK, bh=2)
    #         Node(k=9, c=Color.BLACK, bh=2)
    #             Node(k=8, c=Color.RED, bh=1)
    #             Node(k=10, c=Color.RED, bh=1)
    print(t.delete(5), t.assert_bst_property())
    # True, True
    print(t)
    # Node(k=6, c=Color.BLACK, bh=3)
    #     Node(k=1, c=Color.RED, bh=2)
    #         Node(k=0, c=Color.BLACK, bh=2)
    #         Node(k=3, c=Color.BLACK, bh=2)
    #             Node(k=2, c=Color.RED, bh=1)
    #             Node(k=4, c=Color.RED, bh=1)
    #     Node(k=9, c=Color.RED, bh=2)
    #         Node(k=7, c=Color.BLACK, bh=2)
    #             Node(k=8, c=Color.RED, bh=1)
    #         Node(k=10, c=Color.BLACK, bh=2)
