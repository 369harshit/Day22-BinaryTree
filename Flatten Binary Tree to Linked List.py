class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def flatten(root):
    if root is None:
        return None

    nodes = []
    pre_order_traversal(root, nodes)

    head = ListNode(nodes[0])
    current = head
    for i in range(1, len(nodes)):
        current.next = ListNode(None)
        current = current.next
        current.next = ListNode(nodes[i])
        current = current.next

    return head

def pre_order_traversal(root, nodes):
    if root is None:
        return

    nodes.append(root.val)
    pre_order_traversal(root.left, nodes)
    pre_order_traversal(root.right, nodes)


# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

# Flatten the binary tree into a linked list
result = flatten(root)

# Print the flattened linked list
while result is not None:
    if result.next is not None:
        print(result.val, end=", ")
    else:
        print(result.val)
    result = result.next

# Output: 1, None, 2, None, 3, None, 4, None, 5, None, 6
