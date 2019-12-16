"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # backtracking 
        # set up a recursion
        # at each a* or b* or c* or . or a or b or c,

        # print('entering match') #-------------

        def match(s,reg):
            print('match:', s,',', reg) #-------------------------

            # if length of s and p are 0 then the match is true
            if len(s)==0 or len(reg)==0:
                # print('one of s or reg is zero') #---------------
                if len(s)==0:
                    onlyStars=True
                    for ch in reg:
                        if ch.isupper()==False and ch!=':':
                            onlyStars=False 
                    
                    if len(reg)==0 or onlyStars:
                        matched[0]=True
                        # print('Success!!!!', matched) #-------------------------

            # convert a*-->A, '.*'-->':' in the p string
            # if [A or B or C or :] then, either choose exactly one [a or b or c or .] or choose many
            # many can be written as match s[1:] with the same reg

            elif not matched[0]:
                if reg[0]=='.':
                    match(s[1:], reg[1:])
                elif reg[0]==':':
                    match(s, reg[1:])
                    match(s[1:], reg)
                elif reg[0].islower():
                    if reg[0]==s[0]:
                        match(s[1:], reg[1:])
                else:
                    if reg[0].lower() == s[0]:
                        match(s, reg[1:])
                        match(s[1:], reg)
                        # match(s[1:], reg[1:])
                    else:
                        match(s, reg[1:])

        matched=[False]
        i=0
        lim=len(p)
        while i< lim:
            if p[i]=='*':
                
                if p[i-1]=='.':
                    p= p[:i-1]+ ':' +p[i+1:]
                else:
                    p= p[:i-1]+ p[i-1].upper()+p[i+1:]
                lim-=1
            else:
                i+=1

        match(s,p)

        return matched[0]

sol=Solution()
s="mississippi"
p="mis*is*p*."

# s = "aab"
# p = "c*a*b"

# s = "abcdefghigj"
# p = "abcd*z*w*q*p*.*gj"

s='a'
p='ab*'

# s="bbbba"
# p=".*a*a"

s="aaaaaaaaaaaaab"
p="a*a*a*a*a*a*a*a*a*a*a*a*b"

print(sol.isMatch(s,p))


