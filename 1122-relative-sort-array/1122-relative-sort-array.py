class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sortedA=[]
        for num in arr2:
            while num in arr1:
                sortedA.append(num)
                arr1.remove(num)
        print(sortedA)
        sortedA.extend(list(sorted(arr1)))
        return sortedA

