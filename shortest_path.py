def shortest_path(graph, start, target):
    visited = set()
    queue = [(start, [start])]

    while queue:
        current_node, path = queue.pop(0)
        if current_node == target:
            return path
        visited.add(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print("Path from A to F exists:", shortest_path(graph, start="A", target="F"))
print("Path from D to A exists:", shortest_path(graph, start="D", target="A"))
