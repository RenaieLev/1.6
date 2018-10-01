# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:43:50 2018

@author: Renz
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    #G = nx.read_edgelist("medium.tsv", create_using=nx.DiGraph())
    L = nx.read_edgelist("large.tsv", create_using=nx.DiGraph())
    #Gmaxdistance = 12  # for medium.in
    Lmaxdistance = 100 # for large.in
    #directed_links(G,L)
    #num_users(G,L)
    #connected_components(G,L)
    #avg_cluster_coefficient(G,L)
    #med_compute_distances(G,Gmaxdistance)
    large_compute_distances(L,Lmaxdistance)
"""    
def directed_links(G,L):
    mededges = G.number_of_edges()
    laredges = L.number_of_edges()
    print("The Medium graph consists of", mededges, "Directed Links.")
    print("The Large graph consists of", laredges, "Directed Links.")

    return mededges,laredges

def num_users(G,L):
    medusers = G.number_of_nodes()
    larusers = L.number_of_nodes()
    #print("The Medium graph consists of", medusers, "Users.")
    #print("The Large graph consists of", larusers, "Users.")

    return medusers,larusers

def connected_components(G,L):
    medweak = nx.number_weakly_connected_components(G)
    largeweak = nx.number_weakly_connected_components(L)
    medstrong = nx.nx.number_weakly_connected_components(G)
    largestrong = nx.nx.number_weakly_connected_components(L)
    
    strong_nodesG = [nx.number_of_nodes(Gc) for Gc in nx.strongly_connected_component_subgraphs(G)]
    strong_edgesG = [nx.number_of_edges(Gc) for Gc in nx.strongly_connected_component_subgraphs(G)]
    strong_nodesL = [nx.number_of_nodes(Gc) for Gc in nx.strongly_connected_component_subgraphs(L)]
    strong_edgesL = [nx.number_of_edges(Gc) for Gc in nx.strongly_connected_component_subgraphs(L)]
    
    print("The Medium network contains", medweak, "weakly connected components and", medstrong,"strongly connected components." )
    print("The largest strongly connected component consists of", np.max(strong_nodesG), "nodes and",np.max(strong_edgesG), "edges.")
    print("The Large network contains", largeweak, "weakly connected components and",largestrong,"strongly connected components.")
    print("The largest strongly connected component consists of", np.max(strong_nodesL), "nodes and",np.max(strong_edgesL), "edges.")

    return medweak,largeweak

def avg_cluster_coefficient(G,L):
    medclust= nx.average_clustering(G)
    largeclust = nx.average_clustering(L)
    print ("Average Clustering of Medium Network:",medclust)
    print ("Average Clustering of Large Network:",largeclust)
    
    return medclust, largeclust
""" 
"""
def med_compute_distances(G,Gmaxdistance):  
    Gdistances = np.zeros(Gmaxdistance, dtype=int)
    #Gdistances = max(nx.weakly_connected_components(G), key=len)
    for source in max(nx.weakly_connected_components(G), key=len):
        for target in max(nx.weakly_connected_components(G), key=len):
            if source != target and nx.has_path(G, source, target):
            #Gdistances = max(nx.weakly_connected_components(G), key=len)
                Gdistances[nx.shortest_path_length(G, source, target)] += 1
    print(Gdistances)
    
    # Plot distances #
    fig = plt.figure()
    plt.title("Medium Network Distance Distribution")
    plt.xlabel("Distance")
    plt.xticks(np.arange(0, Gmaxdistance, 1))
    plt.ylabel("Frequency")
    plt.yscale('log')
    plt.bar(np.arange(Gmaxdistance), Gdistances)
    plt.show()
    fig.savefig("Medium_Distance_Distribution.png")
"""
def large_compute_distances(L,Lmaxdistance):  
    Ldistances = np.zeros(Lmaxdistance, dtype=int)
    #Gdistances = max(nx.weakly_connected_components(G), key=len)
    for source in max(nx.weakly_connected_components(L), key=len):
        for target in max(nx.weakly_connected_components(L), key=len):
            if source != target and nx.has_path(L, source, target):
            #Gdistances = max(nx.weakly_connected_components(G), key=len)
                Ldistances[nx.shortest_path_length(L, source, target)] += 1
    #print(Ldistances)
    
    # Plot distances #
    fig = plt.figure()
    plt.title("Large Network Distance Distribution")
    plt.xlabel("Distance")
    plt.xticks(np.arange(0, Lmaxdistance, 1))
    plt.ylabel("Frequency")
    plt.yscale('log')
    plt.bar(np.arange(Lmaxdistance), Ldistances, color=['red'])
    plt.show()
    fig.savefig("Large_Distance_Distribution.png")
    
if __name__ == "__main__":
    main()