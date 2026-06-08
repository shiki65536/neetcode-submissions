class Solution:
    def checkValidString(self, s: str) -> bool:
        opend = []
        star = []

        for i, c in enumerate(s):
            if c == "(":
                opend.append(i)
            elif c == "*":
                star.append(i)
            else:
                if opend:
                    opend.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while opend and star:
            if opend.pop() > star.pop():
                return False
        return True if not opend else False
