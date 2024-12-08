import networkx as nx
import matplotlib.pyplot as plt
import heapq
from colorama import Fore, Style

def dijkstra(G, source):
    distances = {node: float('infinity') for node in G}     # Initialisations
    predecessors = {node: None for node in G} 
    distances[source] = 0  # Set the distance to the starting node as 0
    priority_queue = [(0, source)]  # 1. Priority queue to track nodes and their distances
    subplot_position = 0

    while priority_queue: # 2. Explore nodes in the priority queue until it's empty
        current_distance, current_node = heapq.heappop(priority_queue)
        for neighbor, weight in G[current_node].items(): # 3: Explore neighbors of the current node
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]: #4: Update distance if shorter path is found
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))  # Add to the priority queue

        show_step(predecessors, distances, current_node, priority_queue) # Visualize current state
        subplot_position += 1
        if subplot_position == 1:
            fig = plt.figure()
        draw_step(G, predecessors, current_node, fig, subplot_position)
        if subplot_position  == 5:
            subplot_position = 0

    return distances, predecessors

def draw_step(G, predecessors, current_node,fig, subplot_position):
    pos = nx.spring_layout(G, seed=42)
    fig.add_subplot(1, 5, subplot_position)  # Adjust the subplot grid as needed
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='white')
    for node, pred in predecessors.items(): # Highlight the edges in the shortest path
        if pred is not None:
            nx.draw_networkx_edges(G, pos, edgelist=[(pred, node)], edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='salmon')#Highlight current node
    plt.title(f"Step: {current_node}")

def show_step(predecessors, distances, current_node, priority_queue):
    print(f"Current Node {current_node}: ")
    print(Fore.BLUE+ f"Distances: {distances} \nPredecessors: {predecessors}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Updated Elements: {priority_queue}" + Style.RESET_ALL)
    print(Fore.RED + f"Shortest distance from {source} to {current_node}: {distances[current_node]}" +Style.RESET_ALL)
    path = []
    node = current_node
    while node is not None:
        path.insert(0, node)
        node = predecessors[node]
    print(Fore.RED + "Path:", " -> ".join(path),"\n" + Style.RESET_ALL)

def plot(G):
    fig = plt.figure()     # Plot
    pos = nx.spring_layout(G, seed= 42)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue')
    nx.draw_networkx_nodes(G, pos, nodelist=[source], node_color='salmon') # Highlight the current node
    edge_labels = {(i, j): G[i][j]['weight'] for i, j in G.edges()} # Draw edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

#Inputs
edges = [('0', '1', 4), ('0', '2', 2), ('1', '2', 5), ('1', '3', 10), 
         ('2', '3', 3), ('3', '4', 7), ('5', '6', 8), ('6', '7', 6), 
         ('7', '8', 9), ('8', '9', 12), ('9', '10', 5), ('10', '11', 11), 
         ('11', '12', 4), ('12', '13', 7), ('13', '14', 15), ('14', '5', 13), 
         ('0', '5', 3), ('1', '6', 14), ('2', '7', 1), ('3', '8', 10), 
         ('4', '9', 6), ('5', '10', 8), ('6', '11', 5), ('7', '12', 9), 
         ('8', '13', 7), ('9', '14', 11)]
source = '0'

G = nx.Graph() # Example graph
G.add_weighted_edges_from(edges)

plot(G) #Plot

distances, predecessors = dijkstra(G, source)  # Run Dijkstra's algorithm 

print(f"\nNode\t\tPedecessor\tShortest distance from {source}\n") # Print Distance and predecessor
for i,j in distances.items():
    print(Fore.GREEN + f"  {i}\t\t{predecessors[i]}\t\t{j}" + Style.RESET_ALL)

#plt.tight_layout()
plt.show() 
ArithmeticError
