from node import Node


class AbstractHeuristic:
    def __init__(self):
        """Contuctor method"""

    def eval(self, node):
        """Return value f(b)"""
        pass


class DummyHeuristic(AbstractHeuristic):
    def eval(self, node):
        my_index = Node.PLAYER_1
        enemy_index = Node.PLAYER_2
        return node.get_score(my_index) - node.get_score(enemy_index)
