def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    current = first_node
    seen = set()
    while current:
        if current.value in seen:
            return True
        else:
            seen.add(current.value)
        current = current.next
    return False
