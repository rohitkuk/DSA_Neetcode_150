class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] =1
            else:
                count[num] +=1
         
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        arr.sort(reverse = True)

        return [n for c, n in arr[:k]]