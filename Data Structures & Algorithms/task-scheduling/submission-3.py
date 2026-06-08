class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_tasks = Counter(tasks)
        max_val = max(count_tasks.values())
        max_items = sum([1 for v in count_tasks.values() if  v == max_val])
        res = (max_val - 1) * (n + 1) + max_items
        frame = len(tasks)

        return max(res, frame)

        