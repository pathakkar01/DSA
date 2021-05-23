class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.kSum(nums, 4, target, res, [])
        return res
        
    def kSum(self,nums, k, target, res,result):       
        if k == 2:
            l, h = 0, len(nums)-1
            while l < h :
                s = nums[l] + nums[h]
                if s < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                elif s > target or (h < len(nums)-1 and nums[h] == nums[h+1]):
                    h -= 1
                else:
                    result.append(res + [nums[l], nums[h]])
                    l += 1
                    h -= 1
        else:
            for i in range(0,len(nums)-k+1):
                if len(nums) ==0 or nums[0] * k > target or nums[-1] * k < target:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.kSum(nums[i+1:],k-1, target-nums[i], res+[nums[i]], result)
                
        return
        
        
    
s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))