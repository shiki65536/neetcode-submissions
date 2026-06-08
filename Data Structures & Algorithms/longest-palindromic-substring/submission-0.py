class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        def find(i):
            n = len(s)

            # --- odd palindrome centered at i ---
            # max radius k so that i-k >= 0 and i+k < n
            max_k_odd = min(i, n - 1 - i)
            one = 0
            for k in range(max_k_odd + 1):
                if s[i - k] != s[i + k]:
                    break
                one = k
            odd_str = s[i - one : i + one + 1]

            # --- even palindrome centered between i and i+1 ---
            # only if i+1 exists
            even_str = ""
            if i + 1 < n:
                # max radius k so that i-k+1 >= 0 and i+1+k < n
                max_k_even = min(i + 1, n - (i + 1))  # count of steps possible
                two = 0
                for k in range(max_k_even):
                    if s[i - k] != s[i + 1 + k]:
                        break
                    two = k + 1  # two = length of matched pairs (radius in pairs)

                # if two pairs matched, substring is [i-two+1, i+1+two)
                if two > 0:
                    even_str = s[i - two + 1 : i + 1 + two]

            # pick longer between odd and even
            if len(even_str) > len(odd_str):
                return even_str
            return odd_str


        for i in range(len(s)):
            temp = find(i)
            if len(ans) < len(temp):
                ans = temp

        print(ans)
        return ans         
