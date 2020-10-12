class Matrix:
    def __init__(self, m_1):
        self.m_1 = m_1

    def __add__(self, other):
        new_mat = []
        for i in range(len(self.m_1)):
            new_mat.append([])
            for k in range(len(self.m_1[i])):
                new_mat[i].append(self.m_1[i][k] + other.m_1[i][k])
        return Matrix(new_mat)

    def __str__(self, m_1):
        ent = ""
        for i in self.m_1:
            for k in i:
                ent += k
            ent += "\n"
        return ent


n_1 = Matrix([[3, 4, 2], [3, 1, 7], [5, 7, 5]])
n_2 = Matrix([[1, 2, 3], [2, 3, 1], [4, 2, 3]])
print(n_1+n_2)
