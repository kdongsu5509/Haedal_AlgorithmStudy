#hash
def count_sort(arr,k):
    hashtable=[0]*(k+1)

    for i in arr:
        if i<=k:
            hashtable[i]=1
    return hashtable

def solution(arr,target):
    hashtable=count_sort(arr,target)

    for i in arr:
        num=target-i
        if num!=i and num>=0 and num<=target and hashtable[num]==1:
            return True
    return False
