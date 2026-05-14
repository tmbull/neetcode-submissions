class FirstUnique:
    # need to save first unique number in a queue
    # numbers can't be removed from the queue
    # once a number not unique, we no longer care about it? not true, we also have to save all elements that are not unique
    # so, we need to save uniqueness (set, hashmap) and order (array/list)
    # if there was an ordered set/ordered map, use it

    # python dict is ordered in python 3.7+
    # one dict for uniques
    # one set for non-uniques
    # insertion:
    # look in non-uniques first, if it's there, return
    # look in uniques, if it's there, remove and add to non-uniques
    # if not in uniques, add it

    def __init__(self, nums: List[int]):
        self.uniques = {}
        self.dups = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if not self.uniques:
            return -1
        return next(iter(self.uniques))
        
    def add(self, value: int) -> None:
        if value in self.dups:
            return
        if value in self.uniques:
            del [self.uniques[value]]
            self.dups.add(value)
        else:
            self.uniques[value] = None
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
