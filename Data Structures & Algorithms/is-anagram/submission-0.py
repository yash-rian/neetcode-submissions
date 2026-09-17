class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        character_s= self.char_dict(s)
        character_t= self.char_dict(t)

        if character_s == character_t:
            return True
        else:
            return False
    
    def char_dict(self, st: str):
        char_count={}
        for i in st:
            char_count[i]=char_count.get(i, 0) + 1

        return char_count
