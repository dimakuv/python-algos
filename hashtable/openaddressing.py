# hash table with open addressing (simple, all objects = their int keys)

def hash1(x):
    return x % 11

def hash2(x):
    return x % 7 + 1

DELETED = -1  # assume that hashtable items are always non-negative

class HashTable(object):

    def __init__(self):
        self.n = 0  # number of elements
        self.m = 4  # number of slots, always power of 2
        self.slots = [None] * self.m

    def doublehash(self, x, i):
        return (hash1(x) + i*hash2(x)) % self.m

    def resize(self, newm):
        oldm = self.m
        oldslots = self.slots
        self.m = newm
        self.n = 0
        self.slots = [None] * self.m
        for k in range(oldm):
            if oldslots[k] is not None and oldslots[k] != DELETED:
                self.insert(oldslots[k])

    def search(self, x):
        """returns item index in underlying slots array"""
        i = 0
        while i < self.m:
            idx = self.doublehash(x, i)
            if self.slots[idx] == x:
                return idx
            i += 1
        return None

    def insert(self, x):
        """returns True if successfully inserted (found empty slot and not already present)"""
        res = False
        i = 0
        while i < self.m:
            idx = self.doublehash(x, i)
            if self.slots[idx] == x:
                return False
            if self.slots[idx] == None or self.slots[idx] == DELETED:
                self.slots[idx] = x
                self.n += 1
                res = True
                break
            i += 1
        # need resizing (if half-full or could not insert)
        #   -> rehash all items and move to 2m array
        if res == False or (self.n*100)/self.m >= 50:
            self.resize(self.m*2)
        return res

    def delete(self, x):
        """returns True if successfully deleted (found x)"""
        idx = self.search(x)
        if idx == None:
            return False
        self.slots[idx] = DELETED
        self.n -= 1
        # need resizing (if 1/4-full) -> rehash all items and move to m/2 array
        if self.m > 4 and (self.n*100)/self.m <= 25:
            self.resize(self.m/2)
        return True

def test():
    h = HashTable()
    h.insert(0)
    h.insert(1)	
    h.insert(7)
    h.insert(24)	
    print "after 4 inserts: ", h.slots
    h.insert(42)	
    h.insert(558)	
    h.insert(16961)	
    h.insert(16963)	
    print "after 8 inserts: ", h.slots
    print "searching for 7: ", h.search(7)
    print "searching for 16962: ", h.search(16962)	
    print "searching for 16961: ", h.search(16961)
    h.delete(16963)
    h.delete(16961)	
    h.delete(558)	
    h.delete(42)	
    print "after 4 deletes: ", h.slots
    h.delete(24)	
    h.delete(7)
    h.delete(1)	
    h.delete(0)
    print "after 8 deletes: ", h.slots
