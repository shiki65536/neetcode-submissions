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
        
        for person in range(1, n + 1):
            if len(be_trust[person]) == n - 1 and len(trust_graph[person]) == 0:
                return person
        
        return -1