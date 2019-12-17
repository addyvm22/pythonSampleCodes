"""
https://leetcode.com/problems/interleaving-string/


Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false


"""




import time

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #backtracking 
        #go on assigning 1 or 2 to each char in s3
        #when a letter is assignable to both the strings s1,s2 then choose one and go on, 
        #and then back track if it does not work.
        if len(s3)!=len(s1)+len(s2):
            return False 
        
        global d
        d={}
        return self.interleaveSolution(s1,s2,s3,0,0,0)
        
        
        #setting up the backtracking 
    def interleaveSolution(self, s1, s2, s3, p1,p2,p3):
        #print(p1,p2,p3)
        if (p1,p2,p3) in d.keys():
            return d[(p1,p2,p3)]
        if p3 >= len(s3):
            d[(p1,p2,p3)] = True
            return True
        if p1<len(s1) and s1[p1]==s3[p3]:
            if self.interleaveSolution(s1,s2,s3, p1+1, p2,p3+1):
                d[(p1,p2,p3)] = True
                return True
        if p2<len(s2) and s2[p2]==s3[p3]:
            if self.interleaveSolution(s1,s2,s3, p1, p2+1,p3+1):
                d[(p1,p2,p3)] = True
                return True
        d[(p1,p2,p3)] = False 
        return False 
    
    
s=Solution()
ans=s.isInterleave('aa','bd','aabd')
print(ans)
t1=time.time()
ans2= s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa","babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab","babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")

print(time.time()-t1)
print(ans2)

