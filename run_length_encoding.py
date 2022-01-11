def encode(arr):
    # Code here
    if len(arr)==1:
        return arr+"1"
    i = 0
    ans = []
    while i < len(arr)-1:
        ans.append(arr[i])
        c = 1
        # if arr[i]!=arr[i-1]:
        #     i+=1
        while i<len(arr)-1 and arr[i]==arr[i+1]:
            c+=1
            i+=1
        
        i+=1
        ans.append(str(c))
    if arr[-1]!=arr[-2]:
        ans.append(arr[-1])
        ans.append(str(1))
    ans = "".join(ans)
    return "".join(ans)