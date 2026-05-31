class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.top = None

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node
  
  def pop(self):
    if self.top is None:
      raise IndexError("The stack is empty")
    node = self.top
    self.top = node.next
  
  def print(self):
    if self.top is None:
      raise IndexError("The stack is empty")
    current = self.top
    while current != None:
      print(current.data)
      current = current.next

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()

stack.pop()
stack.print()
