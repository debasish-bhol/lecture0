def maxSubArray(self, A):
        a = A[0]
        b = A[0]
        for i in range(1,len(A)):
            b = max(A[i],A[i]+b)
            a = max(a,b)
        return a
