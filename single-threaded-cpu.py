class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([task + [i] for i, task in enumerate(tasks)])
        
        heap = []
        l = 0
        time = 0
        ans = []

        while l < len(tasks):
            # print(heap, time)
            if not heap:
                # heappush(heap, tasks[l][1:])
                time = max(time, tasks[l][0])

            if tasks[l][0] <= time:
                heappush(heap, tasks[l][1:])
                l+=1
            elif heap:
                finished = heappop(heap)
                time+=finished[0]
                ans.append(finished[1])
            else:
                l+=1

        while heap:
            finished = heappop(heap)
            time+=finished[0]
            ans.append(finished[1])


        return ans