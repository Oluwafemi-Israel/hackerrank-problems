import cProfile


class Node:
    """docstring for Node"""

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
            self.distance_values[node[0]] = node[1]


node0 = Node('0')
node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node('5')
node6 = Node('6')
node7 = Node('7')
node8 = Node('8')

node0.add_adjacent_nodes((node0, 0), (node1, 4), (node7, 8))
node1.add_adjacent_nodes((node1, 0), (node2, 8), (node7, 11))
node2.add_adjacent_nodes((node2, 0), (node3, 7), (node5, 4), (node8, 2))
node3.add_adjacent_nodes((node3, 0), (node2, 7), (node4, 9), (node5, 14))
node4.add_adjacent_nodes((node4, 0), (node3, 9), (node5, 10))
node5.add_adjacent_nodes((node5, 0), (node2, 4), (node3, 14), (node4, 10), (node6, 2))
node6.add_adjacent_nodes((node6, 0), (node5, 2), (node7, 1), (node8, 6))
node7.add_adjacent_nodes((node7, 0), (node0, 8), (node1, 11), (node6, 1), (node8, 7))
node8.add_adjacent_nodes((node8, 0), (node2, 2), (node6, 6), (node7, 7))


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
    print('Next Closest Node:', closest_adjacent_node)

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

    print('Shortest Path Set:', ref_node.shortest_path_set)
    print('Distance Values:  ', ref_node.distance_values)
    print()

    dijkstra(ref_node)


cProfile.run('dijkstra(node0)')
