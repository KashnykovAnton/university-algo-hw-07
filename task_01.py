from tree import Node, insert

def find_max(root):
    if root is None:
        return None
    
    while root.right is not None:
        root = root.right
    
    return root.val

root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

max_value = find_max(root)
if max_value is not None:
    print(f"Maximum value in the tree: {max_value}")
else:
    print("The tree is empty")