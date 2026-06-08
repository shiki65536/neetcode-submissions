class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []
        for s in strs:
            temp.append(s)
            temp.append("｜")

        output = "".join(temp)
        return output


    def decode(self, s: str) -> List[str]:
        output = []
        temp = []
        for c in s:
            if c != "｜":
                temp.append(c)
            else:
                word = "".join(temp)
                output.append(word)
                temp = []
        return output
