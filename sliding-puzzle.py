class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        # q = d([(0,0), (0,1), (0, 2), (1,0), (1,1), (1,2)])
        
        def toTuple(li):
            return tuple(map(tuple, li))

        q = deque([board])
        vis = set([toTuple(board)])
        count = -1
    
        
        while q:
            count+=1
            lvl = len(q)
            # print(q)
            for _ in range(lvl):
                conf = q.popleft()

                if conf == [[1,2,3], [4,5,0]]:
                    return count
                zx = 0 if 0 in conf[0] else 1
                zy = conf[zx].index(0)


                conf[zx][zy], conf[1-zx][zy] = conf[1-zx][zy], conf[zx][zy]
                
                if toTuple(conf) not in vis:
                    q.append(copy.deepcopy(conf))
                    vis.add(toTuple(conf))
                conf[zx][zy], conf[1-zx][zy] = conf[1-zx][zy], conf[zx][zy]
                
                if 0 < zy <= 2:
                    conf[zx][zy], conf[zx][zy-1] = conf[zx][zy-1], conf[zx][zy]
                    if toTuple(conf) not in vis:
                        q.append(copy.deepcopy(conf))
                        vis.add(toTuple(conf))
                    conf[zx][zy], conf[zx][zy-1] = conf[zx][zy-1], conf[zx][zy]
                if 0 <= zy < 2:
                    conf[zx][zy], conf[zx][zy+1] = conf[zx][zy+1], conf[zx][zy]
                    if toTuple(conf) not in vis: 
                        q.append(copy.deepcopy(conf))
                        vis.add(toTuple(conf))
                    conf[zx][zy], conf[zx][zy+1] = conf[zx][zy+1], conf[zx][zy]
        return -1