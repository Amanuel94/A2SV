class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        doms = []
        rep = []

        counter = {}

        for cp in cpdomains:
            rep_dom = cp.split()
            
            domain = rep_dom[1].split('.')
            d = len(domain) - 1
            if domain[d] in counter:
                counter[domain[d]]+=int(rep_dom[0])
            else:
                counter[domain[d]] = int(rep_dom[0])
            d-=1
            if (domain[d]+ "." + domain[d+1]) in counter:
                counter[domain[d]+ "." + domain[d+1]] +=int(rep_dom[0])
            else:
                counter[domain[d]+ "." + domain[d+1]] = int(rep_dom[0])
            d-=1
            if len(domain) > 2:
                if counter.get(domain[d] + "." + domain[d+1]+ "." + domain[d+2], False):
                    counter[domain[d]+ "." + domain[d+1]+ "." + domain[d+2]] +=int(rep_dom[0])
                else:
                    counter[domain[d]+ "." + domain[d+1]+ "."+ domain[d+2]] = int(rep_dom[0])

        return [str(counter[i]) + " " + i for i in counter.keys()]
