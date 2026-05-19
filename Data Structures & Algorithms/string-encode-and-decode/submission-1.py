class Solution:

    def encode(self, strs: List[str]) -> str:
        special = '#'
        ans = ''
        for word in strs:
            ans += str(len(word))
            ans += special
            ans += word
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        finding_len = True
        lenn = ''
        counts = 0
        word = ''
        for i in range(len(s)):
            if finding_len == True:
                if s[i] == '#':
                    finding_len = False
                    counts = int(lenn)
                    lenn = ''
                    if counts == 0:
                        ans.append('')
                        finding_len = True
                else:
                    lenn += s[i]
            else:
                word += s[i]
                counts -= 1
                if counts == 0:
                    finding_len = True
                    ans.append(word)
                    word = ''
        return ans



