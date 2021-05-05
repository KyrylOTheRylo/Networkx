import networkx as nx
import matplotlib.pyplot as plt
import math
my_graph = nx.Graph()
f = open("2.txt","r")
plt.figure(figsize=(8,8))


plt.axes().set_aspect("equal",adjustable="datalim")
G = nx.read_adjlist("2.txt")

nx.draw_circular(G, with_labels=True, font_weight='bold', node_color="black", edge_color="black",font_color="w")
plt.savefig('simple.png')
plt.show()
pos = {x: [float(x)//2, math.sin(float(x)*(math.pi/1.5))] for x in G.nodes()}
pos["8"]=[3.4,0]
pos["9"]=[4.4,-0.1]
pos["10"]=[5.1,0.3]
pos["13"]=[5,2]
nx.draw(G, pos=pos, with_labels=True, font_weight='bold', node_color="black", edge_color="black",font_color="w")
plt.savefig('processed.png')
plt.show()
