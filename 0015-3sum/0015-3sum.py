class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        n = len(A)
        ans = []
        A.sort()
        for i in range(n-2):
            if(i > 0 and A[i] == A[i-1]):
                continue
                
            j,k = i+1, n-1
            while(j < k):
                s = A[i] + A[j] + A[k]
                if(s < 0):
                    j+=1
                elif(s > 0):
                    k-=1
                else:
                    ans.append([ A[i], A[j], A[k] ])
                    
                    while(j < k):
                        if(A[j] == A[j+1]):
                            j+=1
                        else:
                            break
                    while(k > j):
                        if(A[k] == A[k-1]):
                            k-=1
                        else:
                            break
                    j+=1
                    k-=1
        return ans
        