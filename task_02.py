from tree import Node, insert

def find_min(root):
    if root is None:
        return None
    
    while root.left is not None:
        root = root.left
    
    return root.val

root = Node(16)
root = insert(root, 8)
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 1)

min_value = find_min(root)
if min_value is not None:
    print(f"Minimum value in the tree: {min_value}")
else:
    print("The tree is empty")