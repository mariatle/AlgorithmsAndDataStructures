class Solution:
    def similarPairs(self, words: List[str]) -> int:
        my_dict = {}
        for s in words:
            vec = [0] * 26
            for i in range(len(s)):
                #нумерация для букв : а = 0 b = 1 c = 2 и тд z = 25
                vec[ord(s[i]) - ord('a')] = 1
            vec = tuple(vec)
            if vec in my_dict:
                my_dict[vec] += 1
            else:
                my_dict[vec] = 1
        
        ans = 0
        for key in my_dict:
            k = my_dict[key]
            ans += k * (k - 1) // 2
        return ans

