class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = {}
        for anagram in strs:
            key = ''.join(sorted(anagram))
            if key not in output_list.keys():
                output_list[key] = [anagram]
            else:
                output_list[key].append(anagram)
        return list(output_list.values())
