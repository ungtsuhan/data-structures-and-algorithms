def dfs(graph, start_node):
    explored, fronteir = set(), [start_node]
    while fronteir:
        node = fronteir.pop(0)
        if node not in explored:
            explored.update(node)
            print(node)
            fronteir.extend(graph[node] - explored)
    return

def main():
    graph = {"A": set(["B", "C"]),
            "B": set(["A", "D", "E"]),
            "C": set(["A", "F", "G"]),
            "D": set(["B"]),
            "E": set(["B"]),
            "F": set(["C"]),
            "G": set(["C"])
    }
    print(dfs(graph, "A"))

if __name__ == '__main__':
    main()