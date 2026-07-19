class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hashset = set(nums)
        max_len = 1
        for num in nums:
            length = 1
            while length !=0: 
                if num +length in hashset:
                    length +=1
                else:
                    max_len = max(max_len,length )
                    length =0
        return max_len
        