from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, key: T, parent=None, left=None, right=None) -> None:
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right
        self.key: T = key

    def __repr__(self, level=0):
        indent = "    " * level
        repr_str = f"{indent}Node(k={self.key}, h={self.height()}, bf={self.bf()})"
        if self.left:
            repr_str += f"\n{self.left.__repr__(level + 1)}"
        if self.right:
            repr_str += f"\n{self.right.__repr__(level + 1)}"
        return repr_str

    def height(self) -> int:
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1

    def bf(self) -> int:
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return right_height - left_height


class AVL:
    def __init__(self, root: Node = None) -> None:
        self.root = root

    def __repr__(self) -> str:
        return str(self.root)

    def insert(self, k: T) -> bool:
        if self.search(k):
            return False
        self.__insert(Node(k))
        return True

    def __insert(self, z: Node) -> None:
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.__balance(z)

    def delete(self, k: T) -> bool:
        z = self.__search(self.root, k)
        if z is not None:
            self.__delete(z)
            return True
        return False

    def __delete(self, z: Node) -> None:
        q = z.parent
        if z.left is None:
            self.__transplant(z, z.right)
        elif z.right is None:
            self.__transplant(z, z.left)
        else:
            y = self.__minimum(z.right)
            if y.parent != z:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
        self.__balance(q)
        del z

    def __transplant(self, u: Node, v: Node) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def __left_rotate(self, x: Node) -> Node:
        y = x.right
        if y is None:
            return x
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        return y

    def __right_rotate(self, y: Node) -> Node:
        x = y.left
        if x is None:
            return y
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        return x

    def __balance(self, y: Node):
        while y is not None:
            bf = y.bf()
            if bf > 1:
                if y.right.bf() < 0:
                    y.right = self.__right_rotate(y.right)
                y = self.__left_rotate(y)
            elif bf < -1:
                if y.left.bf() > 0:
                    y.left = self.__left_rotate(y.left)
                y = self.__right_rotate(y)
            y = y.parent

    def search(self, k: T) -> bool:
        return self.__search(self.root, k) is not None

    def __search(self, x: Node, k: T) -> Node:
        while x is not None and k != x.key:
            x = x.left if k < x.key else x.right
        return x

    def __minimum(self, x: Node) -> Node:
        while x.left is not None:
            x = x.left
        return x

    def __maximum(self, x: Node) -> Node:
        while x.right is not None:
            x = x.right
        return x

    def in_order_walk(self) -> list[T]:
        return self.__in_order_walk(self.root)

    def __in_order_walk(self, x: Node) -> list[T]:
        return self.__in_order_walk(x.left) + [x.key] + self.__in_order_walk(x.right) if x else []


if __name__ == "__main__":
    t = AVL()
    for i in [9, 5, 1, 0, 6, 3, 2, 4, 7, 8]:
        t.insert(i)
    print(t)
    print(t.in_order_walk())
    print(t.search(10), t.search(9))
    print(t.delete(5))
    print(t)
