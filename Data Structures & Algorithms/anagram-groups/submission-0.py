class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = {}
        for s in strs:
            sortedStr = "".join(sorted(s))

            if sortedStr not in A:
                A[sortedStr] = []
            
            A[sortedStr].append(s)

        return list(A.values())