class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        group =  {i:i for i in range(n)}
        
        def getGroup(i):
            if i == group[i]:
                return i
            group[i] = getGroup(group[i])
            return group[i]

        group[firstPerson] = 0
        meetings.sort(key = lambda k: k[-1])

        # # print(meetings)
        # for person1, person2, time in meetings:
        #     group1 = getGroup(person1)
        #     group2 = getGroup(person2)
        #     # group1, group2 = min(group1, group2), max(group1,group2)
        #     if group1 == 0:
        #         group[group2] = 0
        #     if group2 == 0:
        #         group[group1] = 0

        i = 0
        j = 0
        cur_time = meetings[0][-1]
        while i < len(meetings):
            while i < len(meetings) and meetings[i][-1] == cur_time:

                person1, person2, time = meetings[i]
                group1 = getGroup(person1)
                group2 = getGroup(person2)
                group1, group2 = min(group1, group2), max(group1,group2)
                group[group2] = group1
                i+=1
            
            while j < i:

                person1, person2, time = meetings[j]
                group1 = getGroup(person1)
                group2 = getGroup(person2)
                if group1 != 0:
                    group[person1] = person1
                    group[person2] = person2
                j+=1
            if i < len(meetings):
                cur_time = meetings[i][-1]
                
    

        answer = []
        for person in group:
            if group[person] == 0:
                answer.append(person)  
        return answer