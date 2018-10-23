class Solution(object):
    def optimalDivision(self, nums):
        s=""
        if len(nums)==1:
            return str(nums[0])
        elif len(nums)==2:
            return str(nums[0])+'/'+str(nums[1])
        else:
            if len(nums)==3:
                s=str(nums[0])+'/('+str(nums[1])+'/'+str(nums[2])+')'
            if len(nums)>3:
                s=str(nums[0])+'/('+str(nums[1])+'/'
                for i in range(2,len(nums)-1):
                    s+=str(nums[i])
                    s+='/'
                i+=1
                s+=str(nums[i])+')'    
            return s    
        """
        :type nums: List[int]
        :rtype: str
        """
        