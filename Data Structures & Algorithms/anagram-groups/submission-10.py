class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            mapp[sortedS].append(s)
        return list(mapp.values())

