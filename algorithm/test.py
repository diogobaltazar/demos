from bellman_ford_variation_1 import shortest_paths, build_table
from pydash import py_

G = {
    'a': {'b': 1, 'c': 2},
    'b': {'c': 2, 'd': 10},
    'c': {'d': 2, 'e': 1},
    'd': {},
    'e': {'d': 1},
    'g': {'c': 1},
}

N = 3

H = shortest_paths(G, 3)
n = py_.map(H['c'], lambda _: {list(_)[0]: list(_.values())[0]} )
print(
    H
)

print(build_table(H, 'a', 'c', 'c', n))