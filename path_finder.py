from tree import Node


class KnightPathFinder:
  def __init__(self, position) -> tuple:
    self._root = Node(position)
    self._considered_positions = set(position)

  def get_valid_moves(self, pos):
    directions = [
        (pos[0] - 2, pos[1] - 1),
        (pos[0] - 2, pos[1] + 1),
        (pos[0] + 2, pos[1] + 1),
        (pos[0] + 2, pos[1] - 1),
        (pos[0] - 1, pos[1] - 2),
        (pos[0] - 1, pos[1] + 2),
        (pos[0] + 1, pos[1] - 2),
        (pos[0] + 1, pos[1] + 2)
    ]

    return [(x, y) for x, y in directions if 0 <= x <= 8 and 0 <= y <= 8]

  def new_move_positions(self, pos):
    valid_moves = set(self.get_valid_moves(pos))
    valid_moves -= self._considered_positions
    self._considered_positions.update(valid_moves)
    return valid_moves

  def build_move_tree(self):
    queue = [self._root]
    while len(queue):
      node = queue.pop(0)
      pos = self.new_move_positions(node.value)
      for move in pos:
        child_node = Node(move)
        node.add_child(child_node)
        queue.append(child_node)



finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}
finder.build_move_tree()
