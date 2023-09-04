class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromes(s,left,right) -> int:
            count = 0
            while left >=0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        count = 0
        for i in range (0,len(s)):
           count += countPalindromes(s,i,i)
           count += countPalindromes(s,i,i+1)
        return count
