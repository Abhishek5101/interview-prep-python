def findClosestValueInBst(tree, target):
    return closest_helper(tree, target, tree.value)

def closest_helper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - tree.value) < abs(target - closest):
		closest = tree.value
	if target < tree.value:
		return closest_helper(tree.left, target, closest)
	elif target > tree.value:
		return closest_helper(tree.right, target, closest)
	elif target == closest:
		return closest
	
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
