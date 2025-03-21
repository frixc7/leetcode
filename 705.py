# FIRST SOLUTION

class MyHashSet:

    def __init__(self):
        self.set = []
        

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)
        return

    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)
        return

    def contains(self, key: int) -> bool:
        return key in self.set
