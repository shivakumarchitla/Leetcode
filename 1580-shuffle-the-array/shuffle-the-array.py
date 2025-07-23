class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k = []
        m = len(nums)
        for i in range(m//2):
            c = nums[i]
            k.append(c)
            k.append(nums[i+n])
            
        return k

        