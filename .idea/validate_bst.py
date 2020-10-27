# This is an input class. Do not edit.
"""
Time O(n), Space O(depth)
"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validator(tree, float("-inf"), float("inf"))

def validator(tree, minimum, maximum):
	if tree is None:
		return True
	if tree.value < minimum or tree.value >= maximum:
		return False
	left_is_valid = validator(tree.left, minimum, tree.value)
	right_is_valid = validator(tree.right, tree.value, maximum)
	return left_is_valid and right_is_valid
