# Profiling
# Baseline: 64.1s
# Without head and tail properties: 59.0s
# without next and dropwhile: 11.067s
# with self.level 17s
# only lists 8.8s
# inline ceiling 7.8s
# while loop for node_height: 5.9s

from random import random


class SkipList(object):
    def __init__(self):
        self.tail = ["<TAIL>"]
        self.head = ["<HEAD>", self.tail]

    def __iter__(self):
        node = self.head[1]
        while node is not self.tail:
            yield node[0]
            node = node[1]

    def find_lower(self, search_data, update):
        height = len(self.head)
        node = self.head
        for level in range(height - 1, 0, -1):
            next_node = node[level]

            # 0 is index for data
            while next_node is not self.tail and next_node[0] < search_data:
                node = next_node
                next_node = node[level]

            # update doesn't have a 0 element data
            update[level - 1] = node

        return node

    def add(self, data):
        """Inserts data into appropriate position."""

        # Subtract 1 because the first element of head is data
        head_height = len(self.head) - 1

        # update is an out-parameter from find_lower.  Update is a list of
        # nodes just before the insertion point at each level.
        update = [None] * head_height
        node = self.find_lower(data, update)

        # node_height must be at least 1, so all nodes are reachable at the
        # bottom level, which is a linked list.  That means node[1] always
        # points to the very next node.
        node_height = 1

        # Poor man's Bernoulli distribution, i.e. simulate a coin flip.
        while random() < 0.5:
            node_height += 1

        # Add new levels if the new node_height exceeds head_height because
        # head must be able to reach all nodes.
        for _ in range(node_height - head_height):
            self.head.append(self.tail)
            update.append(self.head)

        new_node = [data]
        for i in range(node_height):
            # Get the node just before new_node at level i with update[i].
            # Then get the node that update[i] is pointing at with
            # update[i][i+1], that node is located after new_node.  We need the
            # +1 because update doesn't have data at update[0], but the node
            # it's pointing at does have data at the 0th index.
            new_node.append(update[i][i + 1])

        for level in range(node_height):
            # Point update at new_node so the chain at level i includes
            # new_node.
            update[level][level + 1] = new_node

    def ceiling(self, search_data):
        """Returns the least element greater than or equal to `search_data`, or None if no
such element exists.

        If `search_data` is None, return None.
        """

        if search_data is None:
            return None

        height = len(self.head)
        node = self.head
        for level in range(height - 1, 0, -1):
            next_node = node[level]

            # 0 is index for data
            while next_node is not self.tail and next_node[0] < search_data:
                node = next_node
                next_node = node[level]

        candidate = node[1]
        if candidate is not self.tail:
            return candidate[0]
        else:
            return None
