inorder = []
postorder = []
preorder = []

def solution(arr):
    arr = [None] + arr
    global inorder, postorder, preorder
    inorder = inorder_traversal(arr, 1)
    postorder = postorder_tr(arr, 1)
    preorder = preorder_tr(arr, 1)

    return [preorder, inorder, postorder]
    # return [inorder, postorder, preorder]

def inorder_traversal(arr, root):
    if root >= len(arr) or arr[root] is None:
        return []
    left = inorder_traversal(arr, root * 2)
    center = [arr[root]]
    right = inorder_traversal(arr, root * 2 + 1)
    return left + center + right

def postorder_tr(arr, root):
    if root >= len(arr) or arr[root] is None:
        return []
    left = postorder_tr(arr, root * 2)
    right = postorder_tr(arr, root * 2 + 1)
    center = [arr[root]]
    return left + right + center

def preorder_tr(arr, root):
    if root >= len(arr) or arr[root] is None:
        return []
    center = [arr[root]]
    left = preorder_tr(arr, root * 2)
    right = preorder_tr(arr, root * 2 + 1)
    return center + left + right

# Test cases
print(solution([1,2,3,4,5,6,7]))
