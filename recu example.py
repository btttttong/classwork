class Node:
  def __init__(self,val,leftNote = None, rightNode = None):
    self.label = val
    self.left = leftNote
    self.right = rightNode
  def isLeaf(self):
      return self.left == None and self.right == None
  def __str__(self):
      if self.isLeaf():
        return "Node({})".format(self.label)
      else:
        return "Node({},{},{})".format(self.label, str(self.left), str(self.right))

  def linearize(self): # Recursive method that return a list of the tree branchs
    if self.isLeaf():
      return [[self]]
    else:
      if self.left != None:
        L1 = self.left.linearize() #recursive processing of the left child node
      else:
        L1 = []
      if self.right != None:
        L2 = self.right.linearize()
      else:
        L2 = []
    return [[self] + e for e in L1] + [[self] + e for e in L2]