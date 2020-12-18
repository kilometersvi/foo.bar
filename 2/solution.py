class node:
    def __init__(self, label):
        self.label = label
        self.right = None
        self.left = None

class tree:
    i = 0

    @staticmethod
    def newnode():
        tree.i += 1
        return node(tree.i)

    #recursively generate perfect binary tree
    @staticmethod
    def gen(h):
        if h == 1:
            return tree.newnode()
        l = tree.gen(h-1)
        r = tree.gen(h-1)
        p = tree.newnode()
        p.left = l
        p.right = r
        return p

    #depth-first search
    @staticmethod
    def search_for_parent(label, c):

        # does current have target label:
        if c.label == label:
            return -1

        # does current have children? if not, skip (assuming perfect)
        if c.left == None:
            return

        # recursively perform search algorithm
        lx = tree.search_for_parent(label, c.left)
        r = c.label if lx == -1 else lx if lx > 0 else None
        if r != None: return r

        rx = tree.search_for_parent(label, c.right)
        return c.label if rx == -1 else rx if rx > 0 else None

def solution(h, q):
    p = tree.gen(h)
    return [tree.search_for_parent(l, p) for l in q]

if __name__ == "__main__":
    print(solution(3, [7, 3, 5, 1]))



'''
#depth-first search
@staticmethod
def search_for_parent(label, p):

    # is p label (can only occur at top level):
    if p.label == label:
        return node(-1)

    # does this node have children? if not, skip
    if p.left == None: #assuming perfect
        return None
    if p.left.label == label or p.right.label == label:
        return p

    # recursively perform search algorithm
    v = tree.search_for_parent(label, p.left)
    if v == None: v = tree.search_for_parent(label, p.right)
    return v
'''
