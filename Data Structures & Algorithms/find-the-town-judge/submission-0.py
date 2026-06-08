class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        be_trust = defaultdict(list)
        trust_graph = defaultdict(list)
        
        for man, candidate in trust:
            be_trust[candidate].append(man)
            trust_graph[man].append(candidate)
        
        sort_be_trust = sorted(be_trust.items(), key=lambda x:len(x[1]), reverse=True)
        
        if len(sort_be_trust[0][1]) != n-1:
            return -1
        
        for candidate in sort_be_trust:
            if len(candidate[1]) != n-1:
                break
            man = candidate[0]
            if len(trust_graph[man]) == 0:
                return man
        
        return -1