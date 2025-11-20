class Solution(object):
    def twoSum(self, nums, target):
        hash_set = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_set:
                return([hash_set[diff], i])
            hash_set[n] = i