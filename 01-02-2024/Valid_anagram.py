"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap={}
        if len(s) != len(t):
            return False
        else:
            for i,j in zip(s,t):
                if i in hashMap:
                    hashMap[i]+=1
                else:
                    hashMap[i]=1
      
                if j in hashMap:
                    hashMap[j]-=1
                else:
                    hashMap[j]= -1
        for val in hashMap.values():
            if val != 0:
                return False
        return True
