from pydash import py_

def shortest_paths(G, N : int = 1):
    """Get the top N shortest paths in G for every possible pair

    The shortest path is computed on the edges' weights

    Arguments:
        G {[type]} -- The network G(E, V)

    Keyword Arguments:
        N {int} -- Number of admissible solutions for path (default: {1})

    Returns:
        [type] -- [description]
    """

    # vertices
    V = G.keys()

    # { destination: [ { code: [ vendor_info ] } ] }
    P = dict()

    edge_weight = lambda v1, v2: py_.filter(G[v1], {'destination': v2})['rate']
    adj_vertex = lambda v: G[v]

    for v in V:
        P[v] = []
    
    for v in V:
        for adj_v in adj_vertex(v):
            adj_v = list(adj_v)[0]
            P[adj_v].append({ 'v': v, 'w': edge_weight(v, adj_v) })
            P[adj_v] = py_.order_by(P[adj_v], 'rate')[0:N]

    for v in V:
        P[v] = py_.map(P[v], lambda _: {_['v']: _['w']})
 
    return P


def aux(graph, key, start):
    if key == start:
        return -1
    else:
        return -1

def build_table(graph, start, end, tmp, res):

    def f(_):
        a = {'test': 1}
        return { **a, **_ }

    return list(map(lambda _: f(_), res))
    

    

