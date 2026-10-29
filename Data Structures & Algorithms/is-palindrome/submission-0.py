class Solution:
    def isPalindrome(self, s: str) -> bool:
        result =''
        for character in s:
            if character.isalnum():
                result += character.lower()
        return result == result[::-1]
        