def generateSubProb(G, tau):
    visited = set()
    for node in G.nodes():
        if node not in visited:
            visited.add(node)
            break
    target_cluster = G.nodes[node]['cluster']
    target_nodes = [n for n in G.nodes() if n not in visited and G.nodes[n]['cluster'] == target_cluster]
    
    while len(target_nodes) <= 2:
        target_nodes = [n for n in G.nodes() if n not in visited]
    
    return target_nodes, target_nodes[0], target_nodes[-1]