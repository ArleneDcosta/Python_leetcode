function invite_party(k, relationships):
    G = create_graph(relationships)
    max_matching = max_matching_k(G, k)
    invited_nodes = set()
    for edge in max_matching:
        invited_nodes.add(edge[0])
        invited_nodes.add(edge[1])
    return invited_nodes

function max_matching_k(G, k):
    max_matching = set()
    for node in G.nodes():
        if G.degree(node) < 2*k:
            neighbors = list(G.neighbors(node))
            if len(neighbors) < k:
                for neighbor in neighbors:
                    G.remove_edge(node, neighbor)
            else:
                matches = hopcroft_karp_matching(G, {node})
                for match in matches:
                    if match[0] == node:
                        max_matching.add(match)
    return max_matching
