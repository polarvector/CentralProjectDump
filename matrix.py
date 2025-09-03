class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])

    def list_construct(self, m, n):
        return [[0 for _ in range(n)] for _ in range(m)]
                

    def __mul__(self, matrixb):
        if self.n != matrixb.m:
            return f"Incompatible dimensions for matrix multiplication: {self.m} x {self.n} | {matrixb.m} x {matrixb.n}"
        result = self.list_construct(self.m, matrixb.n)
        
        for i in range(self.m):
            for j in range(matrixb.n):
                for k in range(self.n):
                    result[i][j] += self.matrix[i][k] * matrixb.matrix[k][j]
        return Matrix(result)

    def __str__(self):
        matreex = f""
        for _ in range(self.m):
            if _ <= self.m - 1:
                matreex += f"\n{self.matrix[_]}"
            else:
                matreex += f"{self.matrix[_]}\n"
        return matreex+"\n"
    
    def __array__(self, dtype=None):
        return np.array(self.matrix, dtype=dtype)