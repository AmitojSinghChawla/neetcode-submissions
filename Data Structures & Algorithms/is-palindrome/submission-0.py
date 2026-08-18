class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = cleaned = "".join(char for char in s if char.isalnum()).lower()

        reversed_string = string[::-1].lower()

        return string == reversed_string
        