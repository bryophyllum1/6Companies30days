class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<1:
            return 0
        count = 0
        curr_pro =1
        j=0
        i= 0
        while j<len(nums):
            curr_pro *= nums[j]
            while curr_pro>=k and i<=j:
                curr_pro//=nums[i]
                i+=1
            
            count += j-i+1
            j+=1
        return count