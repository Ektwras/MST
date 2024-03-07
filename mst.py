
from collections import defaultdict
import heapq


def read_graph(filename):
    graph = defaultdict(list)
    start_node = None

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines[:-1]:
            start, end, weight = line.strip().split()
            weight = int(weight)
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        start_node = lines[-1].strip()

    return graph, start_node



def prims_algorithm(graph, start_node):
    mst = set()
    visited = {start_node}
    edges = [(weight, start_node, to) for to, weight in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        weight, from_node, to_node = heapq.heappop(edges)
        if to_node not in visited:
            visited.add(to_node)
            mst.add((from_node, to_node, weight))
            for next_node, next_weight in graph[to_node]:
                if next_node not in visited:
                    heapq.heappush(edges, (next_weight, to_node, next_node))

    return mst


if __name__ == "__main__":
    input_filename = 'input3.txt'
    output_filename = 'output3.txt'

    graph, start_node = read_graph(input_filename)
    mst = prims_algorithm(graph, start_node)

    total_weight = 0
    with open(output_filename, 'w') as file:
        file.write(f"Minimum Spanning Tree starting from {start_node}:\n")
        for from_node, to_node, weight in mst:
            file.write(f"{from_node} - {to_node} with weight {weight}\n")
            total_weight += weight
        file.write(f"Total weight of MST: {total_weight}\n")

