def invertBinaryTree(tree):
	"""
	Recursive solution
	if tree is None:
		return
    swap_left_and_right_nodes(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
	"""
	queue = [tree]
	while len(queue) > 0:
		current = queue.pop(0)
		if current is None:
			continue
		swap_left_and_right_nodes(current)
		queue.append(current.left)
		queue.append(current.right)
		

	
def swap_left_and_right_nodes(tree):
	tree.left, tree.right = tree.right, tree.left


# This is the class of the input binary tree.
class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
