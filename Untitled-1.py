import numpy as np

def create_matrix(rows, cols):
    """Create a random matrix"""
    return np.random.randint(1, 10, size=(rows, cols))

def matrix_operations(matrix_a, matrix_b):
    """Perform matrix operations"""
    addition = matrix_a + matrix_b
    subtraction = matrix_a - matrix_b
    multiplication = np.dot(matrix_a, matrix_b)
    return addition, subtraction, multiplication

def matrix_transpose(matrix):
    """Get transpose of matrix"""
    return matrix.T

def matrix_determinant(matrix):
    """Calculate determinant"""
    return np.linalg.det(matrix)

def matrix_inverse(matrix):
    """Calculate inverse"""
    return np.linalg.inv(matrix)

# Example usage
if __name__ == "__main__":
    A = create_matrix(6,3)
    B = create_matrix(5,6)
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("Transpose A:\n", matrix_transpose(A)) 