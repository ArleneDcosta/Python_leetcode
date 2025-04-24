from collections import defaultdict

def create_graph(edges):
    parent_to_child = defaultdict(list)
    child_to_parent = defaultdict(list)
    all_nodes = set()

    for rel in edges:
        parent, child = rel.split('->')
        parent = parent.strip()
        child = child.strip()
        parent_to_child[parent].append(child)
        child_to_parent[child].append(parent)
        all_nodes.update([parent, child])

    return parent_to_child, child_to_parent, all_nodes


def merge_siblings(parent_to_child, child_to_parent):
    # Step 1: Reverse mapping from children to (parents, children)
    # This helps us group structurally identical siblings
    node_signature = {}
    print(parent_to_child,child_to_parent)
    for node in set(parent_to_child.keys()).union(child_to_parent.keys()):
        children = tuple(sorted(parent_to_child.get(node, [])))
        parents = tuple(sorted(child_to_parent.get(node, [])))
        sig = (parents, children)
        print(node,sig)
        node_signature.setdefault(sig, []).append(node)
    print(node_signature)
    # Step 2: Merge nodes with same signature
    renamed = {}  # maps old node -> new merged name

    for nodes in node_signature.values():
        if len(nodes) > 1:
            merged_name = ''.join(sorted(nodes))
            for n in nodes:
                renamed[n] = merged_name
        else:
            renamed[nodes[0]] = nodes[0]

    print(renamed)
    # Step 3: Rebuild graph with merged names
    new_graph = defaultdict(list)
    for parent, children in parent_to_child.items():
        new_parent = renamed[parent]
        for child in children:
            new_child = renamed[child]
            if new_child not in new_graph[new_parent]:
                new_graph[new_parent].append(new_child)

    return dict(new_graph)


# --- Example usage
if __name__ == "__main__":
    edges = ['a->b', 'a->c', 'b->d', 'c->d','e->d','e->f']
    p2c, c2p, nodes = create_graph(edges)
    merged = merge_siblings(p2c, c2p)
    print("Merged Graph:")
    for k, v in merged.items():
        print(f"{k} -> {v}")
