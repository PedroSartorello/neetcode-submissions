class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cont = {}
        for num in nums:
            cont[num] = cont.get(num, 0) + 1
        cont = sorted(cont.items(), reverse = True, key=lambda x:x[1])
        res = []
        for i in range(k):
            res.append(cont[i][0])
        return res