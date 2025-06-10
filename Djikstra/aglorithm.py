# Djikstra's Algorithm
import math

# Implement the graph
graph = {}

# Storing the out-neighbors and cost for getting to the neighbor
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {} # The finish node does not have any out-neighbors

# Creating a hash tables to store the current cost for each node (unknown cost = infinity)
infinity = math.inf
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Creating a hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# A Set() is required to keep track of nodes already processed, we do not process nodes more than once
processed = set()

""" Notes / Debugging below """
# Graph["start"] is a hash table with out-neighbors (page 182 visual)
#print(list(graph["start"].keys()))
# Finding the weights of those edges for 'a' and 'b'
#print(graph["start"]["a"])
#print(graph["start"]["b"])

def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        # If its hte lowest cost so far and hasn't been processed yet
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost      # Sets it as the new lowest cost node
            lowest_cost_node = node
        return lowest_cost_node

# Find the lowest cost node you haven't processed yet
node = find_lowest_cost_node(costs)

# If you've processed all the nodes this loop is done
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    # Goes through all out-neighbors of this node if its cheaper to this out-neighbor by going through this node
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 
        if costs[n] > new_cost:  # By going through this node
            costs[n] = new_cost  # Updates the cost for the neighbor 
            parents[n] = node    # This node becomes the new parent for this out-neighbor 
    
    # Marks the node as processed
    processed.add(node)
    # Finds the next node to process and loops
    node = find_lowest_cost_node(costs)
