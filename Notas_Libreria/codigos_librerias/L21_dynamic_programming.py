def binomial(n: int, k: int) -> int:
    # TODO
    pass


def cut_rod(p: list[int], n: int) -> tuple[list[int], list[int]]:
    # TODO
    pass


def lcs(x: str, y: str) -> str:
    # TODO
    pass


if __name__ == "__main__":
    print(binomial(10, 5))
    # 252
    r, s = cut_rod([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 10)
    print(r)
    # [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
    print(s)
    # [None, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10]
    print(lcs("ABCBDAB", "BDCABA"))
    # BCBA
