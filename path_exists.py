def path_exists(graph, start, target):
    if start == target:
        return True
        
    queue = [start]
    visited = {start}

    while queue:
        current_node = queue.pop(0)

        for neighbor in graph.get(current_node, []):
            if neighbor == target:
                return True
                
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}


print("Path from A to F exists:", path_exists(graph, start="A", target="F"))
print("Path from D to A exists:", path_exists(graph, start="D", target="A"))

