import numpy as np

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns: a tuple of two sorted coordinate lists: group and liberties.
    """
    visited = set()
    liberties = set()
    group = set()
    stack = [(row, col)]

    b = np.array(board)

    color = b[row, col]

    while stack:
        r,c = stack.pop()
        if (r,c) in visited:
            continue
        visited.add((r, c))
        group.add((r,c))

        for d_r, d_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_r, n_c = r + d_r, c + d_c
            if 0 <= n_r < b.shape[0] and 0 <= n_c < b.shape[1]:
                if b[n_r, n_c] == color and (n_r, n_c) not in visited:
                    stack.append((n_r, n_c))
                elif b[n_r, n_c] == 0:
                    liberties.add((n_r, n_c))

    sorted_gr = [(r, c) for r, c in sorted(group)]
    sorted_li = [(r, c) for r, c in sorted(liberties)]
    return (sorted_gr, sorted_li)
