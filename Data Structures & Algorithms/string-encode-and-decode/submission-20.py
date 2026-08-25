class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for i in range(len(strs)):
            encoded_string += (str(len(strs[i])) + '#' + strs[i])
            if i == (len(strs)-1):
                return encoded_string
        if strs == []: return ''
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start:end]
            decoded_strs.append(word)
            i = end
        return decoded_strs