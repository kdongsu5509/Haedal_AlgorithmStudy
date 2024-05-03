    result = []
    for i in range(len(cor)) :
        if cor[i] == max(cor) :
            result.append(i+1)
    
    return result