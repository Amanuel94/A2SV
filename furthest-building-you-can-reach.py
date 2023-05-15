class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        # maintain min heap of size ladders
        # if building > heap minimum pop and push, brick - that
        # else brick - that

        heap = []
        i = 0
        while i < len(heights)-1:
            if heights[i+1]-heights[i]>0:
                if ladders > 0:
                    heappush(heap, heights[i+1]-heights[i])
                    ladders-=1
                else:
                    if heap and heights[i+1]-heights[i]> heap[0]:
                        x = heappop(heap)
                        if x > bricks:
                            break
                        bricks-=x
                        heappush(heap, heights[i+1]-heights[i])
                    else:
                        if (heights[i+1]-heights[i]) > bricks:
                            break
                        bricks-=(heights[i+1]-heights[i])
            i+=1
        # while i < len(heights) and heights[i] > heights[i-1]:
        #     i+=1
        return i