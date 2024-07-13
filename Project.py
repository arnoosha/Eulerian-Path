import networkx as nx
import matplotlib.pyplot as plt


def is_bridge(graph, u, v):
    graph.remove_edge(u, v)
    is_connected = nx.has_path(graph, u, v)
    graph.add_edge(u, v)
    return not is_connected


def fleury_algorithm(graph):
    graph_copy = graph.copy()

    odd_degree_nodes = [node for node, degree in graph_copy.degree() if degree % 2 == 1]

    if len(odd_degree_nodes) > 2:
        return None

    start_node = odd_degree_nodes[0] if odd_degree_nodes else list(graph_copy.nodes())[0]

    path = []
    current_node = start_node

    while graph_copy.edges():
        if len(graph_copy[current_node]) == 1:
            next_node = list(graph_copy[current_node])[0]
        else:
            for next_node in graph_copy[current_node]:
                if not is_bridge(graph_copy, current_node, next_node):
                    break
            else:
                next_node = list(graph_copy[current_node])[0]

        path.append((current_node, next_node))
        graph_copy.remove_edge(current_node, next_node)
        current_node = next_node

    return path


edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'E'),
    ('A', 'E'),
    ('A', 'C'),
    ('C', 'D'),
#('C', 'F'),

]

G = nx.Graph()
G.add_edges_from(edges)

eulerian_path = fleury_algorithm(G)
print("Eulerian Path:", eulerian_path)

pos = nx.spring_layout(G)

plt.figure(figsize=(10, 7))

nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=16, font_weight='bold')

if eulerian_path:
    nx.draw_networkx_edges(G, pos, edgelist=eulerian_path, width=4, edge_color='r')

plt.title("Graph with Eulerian Path")
plt.show()
