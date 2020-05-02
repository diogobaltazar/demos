from pydash import py_

def shortest_paths(G, N = 1):
    """[summary]

    Arguments:
        G {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    # vertices
    V = G.keys()

    # { destination: [ { predecessor: shortest_distance } ] }
    P = dict()

    edge_weight = lambda v1, v2: G[v1][v2]
    adj_vertex = lambda v: G[v]
    
    
    for v in V:
        P[v] = []
    
    for v in V:
        for adj_v in adj_vertex(v):
            adj_v = list(adj_v)[0]
            P[adj_v].append({ 'v': v, 'w': edge_weight(v, adj_v) })
            P[adj_v] = py_.order_by(P[adj_v], 'w')[0:N]

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
    

    

