class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows=len(matrix)
        cols=len(matrix[0])
        result=[[0 for i in range(rows)] for j in range(cols)] 
        for i in range(cols):
            row_idx=rows-1 
            col_idx=i 
            for j in range(rows):
                result[i][j]=matrix[row_idx][col_idx]
                row_idx-=1 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=result[i][j]
        return matrix
