class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        answer = []

        l_sum = l_ones = 0
        r_sum = r_ones = 0
        
        i = 0
        while i < len(boxes):
            if int(boxes[i]):
                r_sum += i
                r_ones +=1
            i+=1

        answer.append(r_sum)

        index = 1
        while index < len(boxes):

            if boxes[index-1] == '1':
                l_ones +=1
                r_ones -=1
            l_sum = l_sum + l_ones
            r_sum = r_sum - r_ones

            index+=1
            answer.append(r_sum + l_sum)

        return answer
