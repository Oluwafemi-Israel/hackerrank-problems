# https://www.hackerrank.com/challenges/dijkstrashortreach/problem?h_r=next-challenge&h_v=zen


class Node:
    def __init__(self, node_id):
        self.node_id = node_id

        # list of tuples
        # each tuple represents a reference to an adjacent node and the distance to that node

        self.distance_values = {}

        # set of tuples
        # each tuple represents a reference to a node and the shortest distance to that node
        self.shortest_path_set = set()

    def __repr__(self):
        return '<Node {}>'.format(self.node_id)

    def add_adjacent_nodes(self, *args):
        for node in args:
            if self.distance_values.get(node[0]) is None or 0 <= node[1] < self.distance_values[node[0]]:
                self.distance_values[node[0]] = node[1]


def dijkstra(ref_node):
    # convert the distance value dict to a set of tuples
    distance_values_set = set()
    for key, value in ref_node.distance_values.items():
        distance_values_set.add((key, value))

    # if all nodes have been included in the shortest path set
    if distance_values_set == ref_node.shortest_path_set:
        return ref_node.shortest_path_set

    # get adjacent node with least cost path
    closest_adjacent_node = min(distance_values_set - ref_node.shortest_path_set,
                                key=lambda adjacent_node: adjacent_node[1])
    # print('Next Closest Node:', closest_adjacent_node)

    # add closest_adjacent_node to shortest_path_set set
    ref_node.shortest_path_set.add(closest_adjacent_node)

    # update distance values of nodes adjacent to the recently found closest_adjacent_node
    for key, value in closest_adjacent_node[0].distance_values.items():
        adjacent_node_to_closest_node = (key, value)

        if adjacent_node_to_closest_node[0] in dict(ref_node.distance_values):
            # check if the newly computed distance is less than the existing distance
            if (ref_node.distance_values[closest_adjacent_node[0]] + adjacent_node_to_closest_node[1]) < \
                    ref_node.distance_values[adjacent_node_to_closest_node[0]]:
                ref_node.distance_values[adjacent_node_to_closest_node[0]] = ref_node.distance_values[
                                                                                 closest_adjacent_node[0]] + \
                                                                             adjacent_node_to_closest_node[1]

        else:
            ref_node.distance_values[adjacent_node_to_closest_node[0]] = ref_node.distance_values[
                                                                             closest_adjacent_node[0]] + \
                                                                         adjacent_node_to_closest_node[1]

    # print('Shortest Path Set:', ref_node.shortest_path_set)
    # print('Distance Values:  ', ref_node.distance_values)
    # print()

    dijkstra(ref_node)


# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    # nodes = {node: Node(node) for node in range(1, n + 1)}
    nodes = [Node(node_id) for node_id in range(1, n+1)]

    for edge in edges:
        start = nodes[edge[0]-1]
        end = nodes[edge[1]-1]
        length = edge[2]

        start.add_adjacent_nodes((start, 0), (end, length))
        end.add_adjacent_nodes((end, 0), (start, length))

    source_node = nodes[s-1]
    dijkstra(source_node)

    shortest_distances = source_node.distance_values
    result = []
    for i in range(n):
        shortest_distance = shortest_distances.get(nodes[i])

        if shortest_distance == 0:
            pass
        elif shortest_distance:
            result.append(shortest_distance)
        else:
            result.append(-1)

    return result


if __name__ == "__main__":
    print(shortestReach(4, [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]], 2))
