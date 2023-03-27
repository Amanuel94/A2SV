t  = int(input())
 
 
def merger(nums, l, r, count):
 
    if l == r:
        return nums, count
    mid = (l+r)//2
    left, count_l = merger(nums, l ,mid, count)
    right , count_r = merger(nums, mid+1, r, count)
 
    if count_l == -1 or count_r ==-1:
        return nums, -1
 
    count = count_l+count_r
 
    # print(nums1, l, mid, r, count)
    
    if left[mid] < right[mid+1]:
        return nums, count
    elif left[l] > right[r]:
        i = 0
        while i < r - mid:
            left[l+i], right[mid+1+i] = right[mid+1+i], left[l+i]
            i+=1
        return nums, count+1
    
    else:
        return nums, -1
 
for _ in range(t):
    m  = int(input())
    p = list(map(int, input().split()))
 
    nums, ans =  merger(p, 0, len(p)-1, 0)
 
    print(ans)
