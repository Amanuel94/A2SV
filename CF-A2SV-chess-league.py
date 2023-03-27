n, k = list(map(int, input().split()))
ratings = [(rating, i+1) for i, rating in enumerate(map(int, input().split()))]
 
def merge(left, right):
    ans = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            if right[j][0]-k <= left[i][0]:
                ans.append(left[i])
            i+=1
        else:
            if right[j][0] >= left[i][0]-k:
                ans.append(right[j])
            j+=1
 
    while j < len(right):
        ans.append(right[j])
        j+=1
    while i < len(left):
        ans.append(left[i])
        i+=1
 
    return ans
 
 
def tourn(ratings, l, r, cont = []):
    if l == r:
        return [ratings[l]]
    mid =  (l+r)//2
    left  = tourn(ratings, l, mid, cont)
    right = tourn(ratings, mid+1, r, cont)
 
    return merge(left, right)
 
ans = tourn(ratings, 0, len(ratings)-1)
# print(ans)
print(" ".join(str(i[1]) for i in sorted(ans, key = lambda x:x[1])))
