class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # num rows
        n = len(matrix[0]) # num cols

        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][n - 1]:
                L = 0
                R = n - 1

                while L <= R:
                    mid = (L + R) // 2

                    if target > matrix[i][mid]:
                        L = mid + 1
                    elif target < matrix[i][mid]:
                        R = mid - 1
                    else:
                        return True

        return False


        