class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, int(timestamp)))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.hashmap.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return result
