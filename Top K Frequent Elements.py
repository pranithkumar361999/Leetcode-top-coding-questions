class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=set(nums)
        dictionary={}
        for i in arr:
            dictionary[i]=nums.count(i)
        sorted_dict=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)
        final_dict=dict(sorted_dict)
        val=[]
        for i in final_dict.keys():
            val.append(i)
        return val[:k]


        
