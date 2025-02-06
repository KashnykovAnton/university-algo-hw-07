from tree import Node, insert

def postorder_sum(root):
    if root is None:
        return 0
    left_sum = postorder_sum(root.left)
    right_sum = postorder_sum(root.right)
    return left_sum + right_sum + root.val

root = Node(5)
root = insert(root, 45)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 10)

result = postorder_sum(root)
print("Sum of all values in the tree:", result)