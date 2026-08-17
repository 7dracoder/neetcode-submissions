class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) == len(set(nums)):
        #     return False
        # return True
        dic = {}
        for i in nums:
            if i in dic.keys():
                return True
            dic[i] = 1
        return False

        