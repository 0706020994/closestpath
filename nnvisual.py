import math
import matplotlib.pyplot as plt

# Define the points
a = (0,0)
b = (-3,4)
c = (0,8)
d = (5,-7)
e = (6,3)
f = (4,0)
g = (0,-7)
h = (2,0)

size_nodes = [a, b, c, d, e, f, g, h]

def adjacent(x, nodes):
    closest_distance = float('inf')  # Start with a large number
    closest_node = None
    
    for node in nodes:
        x_diff = x[0] - node[0]
        y_diff = x[1] - node[1]
        distance = math.sqrt(x_diff**2 + y_diff**2)
        
        if distance < closest_distance:
            closest_distance = distance
            closest_node = node

    return closest_node, closest_distance

def visualize(x, nodes):
    # Find the closest node
    closest_node, closest_distance = adjacent(x, nodes)
    
    # Plot all the nodes
    plt.figure(figsize=(8, 8))
    for node in nodes:
        plt.scatter(*node, color='blue')
        plt.text(node[0] + 0.2, node[1] + 0.2, f'{node}', fontsize=12)
    
    # Plot the reference point
    plt.scatter(*x, color='red', label='Reference Point')
    plt.text(x[0] + 0.2, x[1] + 0.2, f'{x}', fontsize=12, color='red')
    
    # Draw lines from the reference point to all other nodes
    for node in nodes:
        plt.plot([x[0], node[0]], [x[1], node[1]], color='gray', linestyle='--')

    # Highlight the closest node
    plt.scatter(*closest_node, color='green', label='Closest Node')
    plt.plot([x[0], closest_node[0]], [x[1], closest_node[1]], color='green')
    plt.text(closest_node[0] + 0.2, closest_node[1] + 0.2, f'{closest_node} (Closest)', fontsize=12, color='green')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Visualization of Nodes and Closest Node')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
reference_point = (-3, -7)
visualize(reference_point, size_nodes)
