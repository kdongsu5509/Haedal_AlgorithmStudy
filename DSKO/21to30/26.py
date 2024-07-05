def solution(arr):
    a = preorder(arr, 0)
    b = inorder(arr, 0)
    c = postorder(arr, 0)

    return [a, b, c]


def preorder(arr, idx):
    temp = ""
    if idx < len(arr):
        temp += str(arr[idx]) + " "
        temp += preorder(arr, idx * 2 + 1)
        temp += preorder(arr, idx * 2 + 2)
    return temp


def inorder(arr, idx):
    temp = ""
    if idx < len(arr):
        temp += inorder(arr, idx * 2 + 1)
        temp += str(arr[idx]) + " "
        temp += inorder(arr, idx * 2 + 2)
    return temp

def postorder(arr, idx):
    temp = ""
    if idx < len(arr):
        temp += postorder(arr, idx * 2 + 1)
        temp += postorder(arr, idx * 2 + 2)
        temp += str(arr[idx]) + " "
    return temp


l = solution([1, 2, 3, 4, 5, 6, 7])
print(l)
