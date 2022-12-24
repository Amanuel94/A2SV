class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners = list(map(lambda x: x[0], matches))
        losers = list(map(lambda x: x[1], matches))

        losers_ = Counter(losers)
        losers_counter = []


        for loser in losers_.keys():
            if losers_[loser] == 1:
                losers_counter.append(loser)

        winners_set = set(winners)
        losers_set = set(losers)

        winners_counter = list(winners_set.difference(losers_set))

        winners_counter.sort()
        losers_counter.sort()

        return [winners_counter, losers_counter]
