class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r=c=0
        direction=1
        m,n=len(mat),len(mat[0])
        result=[]
        for _ in range(m*n):
            result.append(mat[r][c])
            if direction==1:
                if c==n-1:
                    r+=1
                    direction=-1
                elif r==0:
                    c+=1
                    direction=-1
                else:
                    r-=1
                    c+=1
            else:
                if r==m-1:
                    c+=1
                    direction=1
                elif c==0:
                    r+=1
                    direction=1
                else:
                    c-=1
                    r+=1 
        return result
        