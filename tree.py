class Node:
  def __init__(self, value):
    self._value = value
    self._parent = None
    self._children = []

  @property
  def value(self):
    return self._value

  @property
  def children(self):
    return self._children

  def add_child(self, node):
    if node not in self._children:
      self._children.append(node)
      node.parent = self

  def remove_child(self, node):
    if node in self._children:
      self._children.remove(node)
      node.parent = None

  @property
  def parent(self):
    return self._parent

  @parent.setter
  def parent(self, node):
    if self._parent == node:
      return
    if self._parent is not None:
      self._parent.remove_child(self)
    self._parent = node
    if node is not None:
      node.add_child(self)
        
  def depth_search(self, value):
    stack = [self]
    while len(stack):
      current = stack.pop(-1)
      if current._value == value:
        return current
      else:
        stack.extend(current._children)

  def breadth_search(self, value):
    queue = [self]
    while len(queue):
      current = queue.pop(0)
      if current._value == value:
        return current
      else:
        queue.extend(current.children)
    