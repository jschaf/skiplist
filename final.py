# Profiling
# Baseline: 64.1s
# Without head and tail properties: 59.0s
# without next and dropwhile: 11.067s
# with self.level 17s
# only lists 8.8s
# inline ceiling 7.8s
# while loop for node_height: 5.9s


class SkipList(object):

    def __init__(self):
        self.tail = [2**63 - 1]
        self.head = [-2**31, self.tail]


    def find_lower(self, search_data, update):
        height = len(self.head)
        node = self.head
        for level in range(height - 1, 0, -1):
            next_node = node[level]

            # 0 is index for data
            while next_node[0] < search_data:
                node = next_node
                next_node = node[level]

            # update doesn't have a 0 element data
            update[level - 1] = node

        return node


    def insert(self, data):
        """Inserts data into appropriate position."""

        # Subtract 1 because first elem of head is data
        height = len(self.head) - 1

        # update is an out-parameter from find_lower
        update = [None] * height
        node = self.find_lower(data, update)

        node_height = 0
        while random() < 0.5:
            node_height += 1

        # Add new levels if node_height > head
        for _ in range(node_height - height):
            self.head.append(self.tail)
            update.append(self.head)

        new_node = [data]
        for i in range(node_height):
            # Add next levels from update
            new_node.append(update[i][i+1])

        for level in range(node_height):
            # Point update levels at new_node
            update[level][level + 1] = new_node

    def ceiling(self, search_data):
        """Returns the least element greater than or equal to `elem`, or 0 if no such
element exists.

        """
        height = len(self.head)
        node = self.head
        for level in range(height - 1, 0, -1):
            next_node = node[level]

            # 0 is index for data
            while next_node[0] < search_data:
                node = next_node
                next_node = node[level]

        candidate = node[1]
        if candidate is not self.tail:
            return candidate[0]
        else:
            return 0
