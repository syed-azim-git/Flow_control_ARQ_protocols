import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore, Style
	
def BellmanFord(edges, V, src):

	dist = [float("Inf")] * V 	#Initialize distance from src to vertices as INFINITE
	dist[src] = 0

	for _ in range(V): # Relax all edges |V| - 1 times. A shortest path can have at-most |V| - 1 edges 	
		for u, v, w in edges:
			if dist[u] != float("Inf") and dist[u] + w < dist[v]: # Consider only those vertices in queue
				dist[v] = dist[u] + w  # Update dist & parent index of adj vertices of picked vertex.

			if dist[v] != float("Inf") and dist[v] + w < dist[u]: # Interchange u & v - undirected graph
				dist[u] = dist[v] + w
			#print(u,v,w,"\n",dist)

	# Check for negative-weight cycles. The above step guarantees shortest distances if graph doesn't contain
	# negative weight cycle. If we get a shorter path, then there is a cycle. - Directed graph
	for u, v, w in edges:
		if dist[u] != float("Inf") and dist[u] + w < dist[v]:
			print("Graph contains negative weight cycle")
			return

	return dist

def plot(edges,src):
	G = nx.Graph() 
	G.add_weighted_edges_from(edges)
	fig = plt.figure()
	pos = nx.spring_layout(G, seed= 42)
	nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue')
	nx.draw_networkx_nodes(G, pos, nodelist=[src], node_color='salmon') # Highlight the current node
	edge_labels = {(i, j): G[i][j]['weight'] for i, j in G.edges()} # Draw edge labels
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Inputs
V = 15
edges = [(0, 1, 4), (0, 2, 2), (1, 2, 5),
         (1, 3, 10), (2, 3, 3), (3, 4, 7),
         (5, 6, 8), (6, 7, 6), (7, 8, 9),
         (8, 9, 12), (9, 10, 5), (10, 11, 11),
         (11, 12, 4), (12, 13, 7), (13, 14, 15),
         (14, 5, 13), (0, 5, 3), (1, 6, 14),
         (2, 7, 1), (3, 8, 10), (4, 9, 6),
         (5, 10, 8), (6, 11, 5), (7, 12, 9),
         (8, 13, 7), (9, 14, 11)]
src = 0

plot (edges, src)
dist = BellmanFord(edges, V, src) # Find shortest distance from src to vertices using Bellman-Ford algorithm

print(f"\nNode\t\tShortest distance from {src}") #Print
for i in range(V):
	print(Fore.GREEN+f"{i}\t\t{dist[i]}"+Style.RESET_ALL)

#plt.tight_layout()
plt.show() 
ArithmeticError
