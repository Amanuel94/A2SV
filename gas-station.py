class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        net = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(net) < 0:
            return -1
        
        net+=net
        index = 0
        total_cost = 0
        for i, net_cost in enumerate(net):
            total_cost+=net_cost
            if total_cost < 0:
                total_cost = 0
                index = i+1
            if i - index == len(net)//2:
                return index