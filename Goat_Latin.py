class Solution(object):
    def toGoatLatin(self, S):
        vowel=['a','e','i','o','u','A','E','I','O','U']
        s=''
        s1=S.split(" ")
        k=0
        for i in s1:
            
            if i[0] in vowel:
                s+=i+'ma'+'a'*(k+1)
            else:
                 s+=i[1:]+i[0]+'ma'+'a'*(k+1)  
            k+=1        
            s+=" "        
        return s[:len(s)-1]        
        """
        :type S: str
        :rtype: str
        """