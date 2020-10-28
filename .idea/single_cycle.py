def hasSingleCycle(array):
    total_visited = 0
	current_id = 0
	while total_visited < len(array):
		if total_visited > 0 and current_id == 0:
			return False
		total_visited += 1
		current_id = get_next_id(current_id, array)
	return current_id == 0

def get_next_id(current_id, array):
	jump = array[current_id]
	next_id = (current_id + jump) % len(array)
	return next_id if next_id >= 0 else next_id + len(array)