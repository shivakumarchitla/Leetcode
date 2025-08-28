class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        n = 0
        for item in items:
            if ruleKey == "type" and item[0] == ruleValue:
                n+=1
            if ruleKey == "color" and item[1] == ruleValue:
                n+=1
            if ruleKey == "name" and item[2] == ruleValue:
                n+=1
        return n

         