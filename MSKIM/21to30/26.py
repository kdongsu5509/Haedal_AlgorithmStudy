def preorder(nodes,idx):
    if idx<len(nodes):
        result =str(nodes[idx])+" "
        result+=preorder(nodes,idx*2+1)
        result+=preorder(nodes,idx*2+2)
        return result
    else:
        return ""

def inorder(nodes,idx):
    if idx<len(nodes):
        result=inorder(nodes,idx*2+1)
        result+=str(nodes[idx])+" "
        result+=inorder(nodes,idx*2+2)
        return result

    else:
        return ""

def postorder(nodes,idx):
    if idx<len(nodes):
        result=postorder(nodes,idx*2+1)
        result+=postorder(nodes,idx*2+2)
        result+=str(nodes[idx])+" "
        return result
    else:
        return ""

def solution(nodes):
    return [
        preorder(nodes,0)[:-1],
        inorder(nodes,0)[:-1],
        postorder(nodes,0)[:-1],
    ]

nodes=[1,2,3,4,5,6,7]
print(solution(nodes))