class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root == None:
      self.root = Node(data)
    else:
      self.recursive_insert(self.root, data)

  def recursive_insert(self, node, data):
    if data < node.data:
      if node.left == None:
        node.left = Node(data)
      else:
        self.recursive_insert(node.left, data)
    elif node.right == None:
      node.right = Node(data)
    else:
      self.recursive_insert(node.right, data)
  
  def inorder(self):
    if self.root == None:
      raise ValueError("The tree is empty")
    else:
      self.recursive_inorder(self.root)

  def recursive_inorder(self, node):
    if node != None:
      self.recursive_inorder(node.left)
      print(node.data)
      self.recursive_inorder(node.right)

tree = BinaryTree()
tree.insert(15)
tree.insert(10)
tree.insert(25)
tree.insert(-3)
tree.insert(60)

tree.inorder()