# Cell 1
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    
    if len(a) != len(b):
        return -1
    
    dot_product = []
    for i, row in enumerate(a):
        running_sum = 0
        for j, element in enumerate(row):
            running_sum += row[j] * b[j]
            # print(row[j], "*", b[j])
        dot_product.append(running_sum)
    
    return dot_product
        
        
a = [[1, 2], [2, 4]]
b = [1, 2]

matrix_dot_vector(a,b)