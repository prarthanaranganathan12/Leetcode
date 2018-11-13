class Solution(object):
    def stoneGame(self, piles):
        alex=0
        lee=0
        i=0
        while(i<len(piles)-1):
            alex+=piles[i]
            lee+=piles[i+1]
            i+=2
        if alex<lee:
            alex=0
            lee=0
            i=len(piles)-1
            while(i>0):
                alex+=piles[i]
                lee+=piles[i-1]
                i-=2
            return alex>lee
        else:
            return alex>lee

