class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def isAcheiveable(req_dict):
            
            for key in req_dict:
                if req_dict[key]:
                    return False
            return True
        
        max_ = float('-inf')
        
        def transfer_net(requests, cur, req_dict, n):
            nonlocal max_
            if cur == len(requests):
                
                if isAcheiveable(req_dict):
                    max_ = max(max_, n)
                return
            
            
            
            
            req_dict[requests[cur][0]]+=1
            req_dict[requests[cur][1]]-=1
            
            transfer_net(requests, cur+1, req_dict, n+1)
            req_dict[requests[cur][0]]-=1
            req_dict[requests[cur][1]]+=1
            
            transfer_net(requests, cur+1, req_dict, n)
            
        transfer_net(requests, 0, defaultdict(int), 0)
        return max_      
