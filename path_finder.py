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
    return valid_moves - self._considered_positions

  def build_move_tree(self):
    valid_moves = self.new_move_positions(self._root.value)
    for move in valid_moves:
      child_node = Node(move)
      self._root.add_child(child_node)
    print([x.value for x in self._root.children])


finder = KnightPathFinder((4, 4))
finder.build_move_tree()
print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}
