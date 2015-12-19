class LLRB(object):

    class Node(object):
        RED = True
        BLACK = False

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.color = LLRB.Node.RED


        def flip_colors(self):
            self.color = not self.color
            self.left.color = not self.left.color
            self.right.color = not self.right.color


    def __init__(self):
        self.root = None


    def ceiling(self, value):
        """Return the smallest item greater than or equal to value.  If no such value
        can be found, return None.

        """
        x = self.root
        best = None
        while x is not None:
            if x.value == value:
                return value
            elif x.value > value:
                best = x.value if best is None else min(best, x.value)
                x = x.left
            else:
                x = x.right

        return best


    @staticmethod
    def is_red(node):
        if node is None:
            return False
        else:
            return node.color == LLRB.Node.RED


    def add(self, value):
        self.root = LLRB.insert_at(self.root, value)
        self.root.color = LLRB.Node.BLACK


    @staticmethod
    def insert_at(node, value):
        if node is None:
            return LLRB.Node(value)

        if LLRB.is_red(node.left) and LLRB.is_red(node.right):
            node.flip_colors()

        if node.value == value:
            node.value = value
        elif node.value < value:
            node.left = LLRB.insert_at(node.left, value)
        else:
            node.right = LLRB.insert_at(node.right, value)


        if LLRB.is_red(node.right) and not LLRB.is_red(node.left):
            node = LLRB.rotate_left(node)
        if LLRB.is_red(node.left) and LLRB.is_red(node.left.left):
            node = LLRB.rotate_right(node)

        return node


    @staticmethod
    def rotate_left(node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = LLRB.Node.RED
        return x


    @staticmethod
    def rotate_right(node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = LLRB.Node.RED
        return x
