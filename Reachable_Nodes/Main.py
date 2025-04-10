def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    queue = []
    visited = set()
    queue.append(start_node)
    while True:
        adj_list, queue, visited = indexQueue(adj_list, queue, visited)
        if not queue:
            break

    return visited


def indexQueue(adj_list, queue, visited):
    temp = queue[0]
    if temp not in visited:
        visited.add(temp)
        for j in adj_list[temp]:
            if j not in visited:
                queue.append(j)

    queue.pop(0)
    return adj_list, queue, visited