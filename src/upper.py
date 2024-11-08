import mdptoolbox as mdpt
import mdptoolbox.example
import numpy as np


def naiveClusterSolving(G, tau):
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


def generateSubProb(G, tau, mdp):
    
    # use mdp to solve subproblem
    mdp.run()
    # print('optimal_policy:', mdp.policy)
    # print('optimal_value_function:', mdp.V)
    # TODO order subset of nodes according to policy

    return naiveClusterSolving(G, tau)
