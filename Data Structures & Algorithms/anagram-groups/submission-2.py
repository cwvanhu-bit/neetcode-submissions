class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for char in i:
                count[(ord(char) - ord("a"))] += 1

            letters[tuple(count)].append(i)

        x = list(letters.values())
        return x