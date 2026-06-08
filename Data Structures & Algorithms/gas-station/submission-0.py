class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost or len(gas) != len(cost):
            return -1
        
        n = len(gas)
        
        def trip(idx):
            tank = 0
            for i in range(n):
                j = (idx + i) % n
                print(tank)
                tank += gas[j] - cost[j]
                print(tank)
                if tank < 0:
                    return False
            return True
                

        for i in range(n):
            if trip(i):
                return i
        
        return -1