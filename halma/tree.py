class Tree(object):
    def __init__(self, children=None, score=0, state=None):
        self.score = score
        self.state = state
        self.children = children

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.add(node)
