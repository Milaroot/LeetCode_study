class MyHashSet:
    
    def __init__(self):
        self.mp = defaultdict(int)

    def add(self, key: int) -> None:
        self.mp[key] = 1

    def remove(self, key: int) -> None:
        self.mp[key] = 0

    def contains(self, key: int) -> bool:
        return self.mp[key]   


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)