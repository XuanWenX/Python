from random import randint
class Die:

    def __init__(self, nums=6):
        self.nums = nums

    def roll(self):
        return randint(1, self.nums)


