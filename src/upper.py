def generateSubProb(G, tau):
    # print('running generateSubProb')
    # finding target cluster
    for node in G.nodes():
        if G.nodes[node]['visited'] is False:
            break
    target_cluster = G.nodes[node]['cluster']
    target_nodes = [n for n in G.nodes() if G.nodes[n]['visited'] is False and G.nodes[n]['cluster'] == target_cluster]
    
    # Ensure target_nodes has at least 3 nodes
    if len(target_nodes) < 3:
        for node in G.nodes():
            if G.nodes[node]['visited'] is False and node not in target_nodes:
                target_nodes.append(node)
                if len(target_nodes) >= 3:
                    break

    return target_nodes, target_nodes[0], target_nodes[-1]
