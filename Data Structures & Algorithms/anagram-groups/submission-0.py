class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lets_to_words = {}
        seen_dicts: List[dict[str,int]] = []
        for word in strs:
            letters = {}
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
            if letters in seen_dicts:
                ind = seen_dicts.index(letters)
                lets_to_words[ind].append(word)
            else:
                seen_dicts.append(letters)
                ind = seen_dicts.index(letters)
                lets_to_words[ind] = [word]
        ans = []
        for key, value in lets_to_words.items():
            ans.append(value)
        return ans
