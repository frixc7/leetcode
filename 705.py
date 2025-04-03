class MyHashSet:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.hashset = [None, None]
        
    def hashing(self, key): # works
        # sum each char's ASCII value then mod by capacity
        return sum(ord(c) for c in key) % self.capacity
    
    def rehashing(self): # works
        # double the size of the capacity
        self.capacity *= 2
        new_set = [None] * self.capacity
        old_set = self.hashset
        self.hashset = new_set
        
        self.size = 0
        # rehash each key and add it to the new set
        for i in old_set:
            if i != None:
                self.add(i)

    def add(self, key: int) -> None: # works, but doesn't check whether it exists after a hole, the solution is to use contains, but this makes it O(n). In the description, it was not specified what the program should do if the value already exists. But it still fails if you add it when it already exists (it's a set).
        if self.contains(key) == False:
            index = self.hashing(key)
            while True:
                # if its not in and index is empty, add
                if self.hashset[index] == None:
                    self.hashset[index] = key
                    self.size += 1
                    break

                # if there's already another value in, open address
                index += 1
                index %= self.capacity
            
            if self.size == self.capacity // 2: # rehashing when capacity is half full
                self.rehashing()

    def remove(self, key: int) -> None: # works
        index = self.hashing(key)
        
        while index <= self.capacity - 1: # this key might appear after index (index is at 10 and capacity is 12 so it keeps going through indices until let's say index 3 which is empty. This is in case a lot of collisions happen.)
            # if its at index, remove
            if self.hashset[index] == key:
                self.hashset[index] = None
                self.size -= 1
                break
            
            # keep incrementing until you find it
            index += 1
            index %= self.capacity
            
    def contains(self, key: int) -> bool: # works
        # check the index and every index after it until the end
        
        index = self.hashing(key)
        
        while index < self.capacity - 1:
            if self.hashset[index] == key:
                return True
            
            index += 1
            index %= self.capacity
            
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
