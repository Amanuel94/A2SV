class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        """ 
        any permutaion of length n can be written as a product of n-1 transpositions,
        thus just count the indices that are not covered by the allowable swaps
        """
        n = len(source)
        group = {i:i for i in range(n)}
        
        def getGroup(i):
            if i == group[i]:
                return i
            group[i] = getGroup(group[i])
            return group[i]

        # connect swaps that share positions
        visited_positions ={}
        for i, swaps in enumerate(allowedSwaps):
            ai, bi = swaps
            group[getGroup(ai)] = getGroup(bi)
 
        
        # construct a counter for each representative
        members = defaultdict(dict)
        for i in range(n):
            if source[i] in members[getGroup(i)]:
                members[getGroup(i)][source[i]]+=1
            else:
                members[getGroup(i)][source[i]] = 1
        hamming_dist = 0

        for i in range(n):
            if target[i] == source[i]:
                members[getGroup(i)][target[i]]-=1
                
        for i in range(n):
            if  target[i]!=source[i] and (target[i] not in members[getGroup(i)] or members[getGroup(i)][target[i]]<1):
                hamming_dist+=1
            elif members[getGroup(i)][target[i]]>0 and target[i]!=source[i]:
                members[getGroup(i)][target[i]]-=1
         

        return hamming_dist