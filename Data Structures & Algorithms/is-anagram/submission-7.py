# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         if len(s) != len(t):
#             return False

#         freqCounterS = {}
#         freqCounterT= {}

#         for key in s:
#             freqCounterS[key] = freqCounterS.get(key,0)+1
        
#         for key in t:
#             freqCounterT[key] = freqCounterT.get(key,0)+1

#         return freqCounterS == freqCounterT        



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False
        
        from collections import Counter
        return Counter(s) == Counter(t)