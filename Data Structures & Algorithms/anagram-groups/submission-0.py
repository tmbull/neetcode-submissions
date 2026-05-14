class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # define a dict that can map 'key' to [anagram]
        # key is sorted str
        results: dict[str,List[str]] = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in results:
                results[ss].append(s)
            else:
                results[ss] = [s]
        return results.values()