import networkx as nx
import matplotlib.pyplot as plt
import math
import random


def set_own_pos():
    pos = {x: [float(x) // 2, math.sin(float(x) * (math.pi / 1.5))] for x in G.nodes()}
    pos["8"] = [3.4, 0]
    pos["9"] = [4.4, -0.1]
    pos["10"] = [5.1, 0.3]
    pos["13"] = [5, 2]
    return pos


def new_edges(tuple_):
    tmp_node = []
    for elements in tuple_:
        for node_ in elements:
            if node_ not in tmp_node:
                tmp_node.append(node_)
    G.remove_edges_from(tuple_)

    nx.draw(G, pos=set_own_pos(), with_labels=True, font_weight='bold', node_color="black", edge_color="black",
            font_color="w")
    G.add_edges_from(tuple_)

    nx.draw_networkx_edges(G, pos=set_own_pos(), edgelist=tuple_, edge_color='r')
    return tmp_node


def part3_4():
    n = 1
    tmp_edges_global = []
    with open("output.txt", 'w') as out:

        for x in (nx.connected_components(G)):
            tmp = nx.subgraph(G, x)

            print(f"-------Begin of the component {n}-------")
            out.writelines(f"-------Begin of the component {n}-------")
            x = sorted(x, key=float)

            print(f'nodes = {len(x)} ')
            out.writelines(f'nodes = {len(x)} ')
            print(f'edges = {len(G.edges(x))}')
            out.writelines(f'edges = {len(G.edges(x))}')
            eccentr = nx.eccentricity(tmp)
            for node_ in x:
                print(f"~~~~~~~~Node {node_}~~~~~~~~")
                out.writelines("~~~~~~~~Node {node_}~~~~~~~~")
                print(f'''degree: {G.degree[node_]}''')
                out.writelines(f'''degree: {G.degree[node_]}''')
                print(f'''eccentricity: {eccentr[node_]}''')
                out.writelines(f'''eccentricity: {eccentr[node_]}''')
            print("")
            out.writelines("")
            diam = nx.diameter(tmp, eccentr)
            print(f'''Radius of the component {n} = {nx.radius(tmp, eccentr)}''')
            out.writelines(f'''Radius of the component {n} = {nx.radius(tmp, eccentr)}''')
            print(f'''Diameter of the component {n} = {diam}''')
            out.writelines(f'''Diameter of the component {n} = {diam}''')
            tmp_edges = []

            for node1 in x:
                for node2 in x:
                    for path in (nx.all_simple_edge_paths(tmp, node1, node2)):
                        if len(list(path)) == diam:
                            tmp_edges.append(path)
            random_edges = random.choice(tmp_edges)
            tmp_edges_global.extend(random_edges)

            print(f"--------End of the component {n}--------\n")
            out.write(f"--------End of the component {n}--------\n")
            n += 1

    tmp_node = new_edges(tmp_edges_global)
    nx.draw_networkx_nodes(G, pos=set_own_pos(), nodelist=tmp_node, node_color='r')


"""
PART 1
"""
my_graph = nx.Graph()
f = open("data.txt", "r")
plt.figure(figsize=(8, 8))

plt.axes().set_aspect("equal", adjustable="datalim")
G = nx.read_adjlist("data.txt")

nx.draw_circular(G, with_labels=True, font_weight='bold', node_color="black", edge_color="black", font_color="w")
plt.savefig('simple.png')
plt.show()
plt.close()

"""
PART 2
"""

nx.draw(G, pos=set_own_pos(), with_labels=True, font_weight='bold', node_color="black", edge_color="black",
        font_color="w")
plt.savefig('processed.png')
plt.show()
plt.close()
"""
PART 3-4
"""

part3_4()
plt.savefig('diam.png')
plt.show()
plt.close()
"""
PART 5
"""
tmp_edges = []
for el in (nx.dfs_edges(G)):
    tmp_edges.append(el)
new_edges(tmp_edges)
plt.savefig('forest.png')
plt.show()
plt.close()
