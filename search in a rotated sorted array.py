class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=nums[0]
        last=nums[-1]
        if target not in nums:
            return -1
        fp=0
        lp=len(nums)-1
        if last<first:
            while True:
                if target==nums[lp]:
                    return lp
                else:
                    lp-=1
        else:
            while True:
                if target==nums[fp]:
                    return fp
                else:
                    fp+=1
        
