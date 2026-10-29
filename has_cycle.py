def has_circle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        rec_stack.remove(node)
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True

    return False

graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}
print(has_circle(graph))