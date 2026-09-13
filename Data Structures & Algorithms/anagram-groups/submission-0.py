class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Two strings are anagrams exactly when their sorted versions match,
        # so the sorted version of a string works as a shared name for a whole group of strings.
        # We can make a map whose keys are those sorted versions.
        # Then for each string we check if its sorted version is already a key.
        # If it is, we've already seen an anagram of this string, and the list under
        # that key is that group, so appending the unsorted string puts it with its group.
        # If it isn't, this string is the first of its group, so we start an empty list
        # under that key for it and its future anagrams to land in.
        # At the end of it all, every group lives in its own list, so we can return
        # an array of all the values of the map.

        A = {}
        for s in strs:
            sortedStr = "".join(sorted(s))

            if A.get(sortedStr) == None: # Nothing has sorted to this before, so nothing exists to append to yet
                A[sortedStr] = []

            A[sortedStr].append(s) # Everything under this key sorted to the same thing, so they're all anagrams

        return list(A.values())