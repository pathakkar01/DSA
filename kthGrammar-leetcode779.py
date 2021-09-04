class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1 and K==1:
            return 0
        mid = (2 ** (N-1))/2
        if K <= mid:
            return self.kthGrammar(N-1, K)
        else:
            return int(not(self.kthGrammar(N-1, K-mid)))
 """
 isSame=1
    for i in range(N-1):
        if K%2 == 0 :
            isSame = -isSame
            K/=2
        else:
            K=(K+1)/2
    return 0 if isSame == 1  else 1 """
 
            
  
        
