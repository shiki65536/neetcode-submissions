class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        best = 1
        count = 1
        prev = ""
        for i in range(1, len(arr)):

            if arr[i-1] < arr[i] and prev == ">":
                prev = "<"
                count += 1
            elif  arr[i-1] > arr[i] and prev == "<":
                prev = ">"
                count += 1
            else:
                if arr[i-1] < arr[i]:
                    prev = "<"
                    count = 2
                elif arr[i-1] > arr[i]:
                    prev = ">"
                    count = 2
                else:
                    prev = ""
                    count = 1
            best = max(best, count)
        
        return best
