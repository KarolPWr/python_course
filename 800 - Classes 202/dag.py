class Dag:
    """https://en.wikipedia.org/wiki/Directed_acyclic_graph
    not https://www.youtube.com/watch?v=zH64dlgyydM
    """
    def __init__(self):
        self._allowed_pairs = set()
        self._recently_added_node = None

    def __call__(self, entry_point):
        self._allowed_pairs.add((None, entry_point))
        self._recently_added_node = entry_point
        return self

    def __rshift__(self, node):
        """There is direct edge from self._recently_added_node to node
        """
        self._allowed_pairs.add((self._recently_added_node, node))
        self._recently_added_node = node
        return self  # we have to return DAG instance

    def is_direct_path(self, *paths):
        """reimplement `is_direct_path` so it will be able to detect path of unlimited length"""
        # return (deriving, to) in self._allowed_pairs
        pairs = list(self.split_path_to_pairs(paths))
        for pair in pairs:
            if pair not in self._allowed_pairs: # not working?
                return False

    def split_path_to_pairs(self, *paths):
        for i in range(0, len(paths), 2):  #create pairs
            yield paths[i:i+2]

    def is_start_node(self, node):
        return self.is_direct_path(None, node)


if __name__ == '__main__':
    dag = Dag()

    # only one node (1)
    dag(1)
    assert dag.is_start_node(1)

    # Exercise1: add edge 1 -> 2
    dag(1) >> 2
    assert dag.is_direct_path(1, 2)
    assert not dag.is_direct_path(2, 1)
    assert not dag.is_start_node(2)

    dag(0) >> 1
    assert dag.is_start_node(0)
    assert dag.is_start_node(1)
    assert dag.is_direct_path(0, 1)

    # Exercise2: Make sure that >> operator can be chained
    dag(0) >> 1.1 >> 2
    dag(0) >> 1.2 >> 2 >> 3 >> 4
    assert dag.is_direct_path(0, 1.1)
    assert dag.is_direct_path(0, 1.2)
    assert dag.is_direct_path(1.1, 2)
    assert dag.is_direct_path(1.2, 2)

    # Exercise3: reimplement `is_direct_path` so it will be able to detect path of unlimited length
    assert dag.is_direct_path(0, 1, 2, 3, 4)

    # *Exercise4: Bonus (1 -> 2.1), (1 -> 2.2), (2.1 -> 3), (2.2 -> 3)
    dag(1) >> (2.1, 2.2) >> 3
    assert dag.is_direct_path(1, 2.1, 3)
    assert dag.is_direct_path(1, 2.2, 3)

    # *Exercise5:
    assert dag.is_direct_path(1, (2.1, 2.2), 3)
