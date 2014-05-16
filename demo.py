import networkx as nx
from matplotlib import pyplot as plt

def gen_connected_network(g, vs):
    """
        generate subgraph containing only given node set vs
        input:
            @g: original graph
            @vs: visible node set
        output:
            @new_g: subgraph
    """
    new_g = nx.Graph()
    for v1 in vs:
        for v2 in vs:
            if v1 == v2:
                continue
            else:
                if not new_g.has_edge(v1, v2) and g.has_edge(v1, v2):
                    new_g.add_edge(v1, v2)
    return new_g

def main(graph_filename):
    """
        plot the core information network
    """

    # read graph from file
    G = nx.read_edgelist(graph_filename, data=False)

    # calculating closeness
    closeness_dict = nx.closeness_centrality(G)

    core_k = 50
    core_nodes = [ v for v, centrality in sorted(closeness_dict.items(), key=lambda x: x[1],reverse=True)[:core_k] ]
    core_G = gen_connected_network(G, core_nodes)

    # plot graph
    layout = nx.spring_layout(core_G, iterations=100)
    nx.draw_networkx(core_G, layout, edge_color='b', style="dashed", node_size=2000, node_color="w")
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()

if __name__ == "__main__":
	main("data/tw_company.txt")
