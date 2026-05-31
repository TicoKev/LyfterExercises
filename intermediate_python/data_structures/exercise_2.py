class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
  
class DoubleEndedQueue:
  def __init__(self):
    self.head = None
    self.tail = None

def push_left(self, data):
  new_node = Node(data)
  
  if self.head == None:
    self.head = new_node
    self.tail = new_node
  else:
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

def push_right(self, data):
  new_node = Node(data)

  if self.tail == None:
    self.tail = new_node
    self.head = new_node
  else:
    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node

def pop_left(self):
  if self.head == None:
    raise IndexError("The dequeue is empty")

  current = self.head
  self.head = current.next
  if self.head:
    self.head.prev = None
  else:
    self.tail = None
  
def pop_right(self):
  if self.head == None:
    raise IndexError("The dequeue is empty")

  current = self.tail
  self.tail = current.prev
  if self.tail:
    self.tail.next = None
  else:
    self.head = None

