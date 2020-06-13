# Define the main function, which get the users input till exit option is used
def main():
    ticker = True
    while ticker:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n"
              "4. Transpose matrix\n5. Calculate a determinant\n6. Inverse Matrix\n0. Exit")
        choice = int(input("Your choice: "))
        if choice == 1:
            add_matrices()
        elif choice == 2:
            multiply_by_constant()
        elif choice == 3:
            multiply_two_matrices()
        elif choice == 4:
            transpose_call()
        elif choice == 5:
            determinant_call()
        elif choice == 6:
            inverse_call()
        elif choice == 0:
            ticker = False
    print("program finished")

# Define function to add to matrices
def add_matrices():
    matrix_A = []
    matrix_B = []
    matrix_C = []

    size_int_A = input("Enter size of first matrix: ")
    rows = int(size_int_A.split(" ")[0])
    columns = int(size_int_A.split(" ")[1])
    print("Enter first matrix:")
    for j in range(rows):
        matrix_A.append([float(x) for x in input().split(" ")])

    size_int_B = input("Enter size of second matrix: ")
    print("Enter second matrix:")
    for j in range(rows):
        matrix_B.append([float(x) for x in input().split(" ")])

    if size_int_A != size_int_B:
        print("Matrices must be of the same size")
        return

    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(matrix_A[i][j] + matrix_B[i][j])
        matrix_C.append(temp)
    print("The result is:")
    for i in range(rows):
        for j in range (columns):
            print(matrix_C[i][j], end =" ")
        print("")
    print("")

# Define function to multiply matrix by a constant
def multiply_by_constant():
    matrix_A = []
    matrix_C = []

    # Get the first matrix
    size_int_A = input("Enter size of first matrix: ")
    rows = int(size_int_A.split(" ")[0])
    columns = int(size_int_A.split(" ")[1])
    print("Enter first matrix:")
    for j in range(rows):
        matrix_A.append([float(x) for x in input().split(" ")])

    # Get the constant
    const = float(input("Enter constant: "))

    # Calculate the resulting matrix
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(matrix_A[i][j] * const)
        matrix_C.append(temp)

    # Print out the resulting matrix
    print("The result is:")
    for i in range(rows):
        for j in range(columns):
            print(matrix_C[i][j], end =" ")
        print("")
    print("")

def multiply_two_matrices():
    matrix_A = []
    matrix_B = []
    matrix_C = []

    size_int_A = input("Enter size of first matrix: ")
    rows_A = int(size_int_A.split(" ")[0])
    columns_A = int(size_int_A.split(" ")[1])
    print("Enter first matrix:")
    for j in range(rows_A):
        matrix_A.append([float(x) for x in input().split(" ")])
    #print(matrix_A)

    size_int_B = input("Enter size of second matrix: ")
    print("Enter second matrix:")
    rows_B = int(size_int_B.split(" ")[0])
    columns_B = int(size_int_B.split(" ")[1])
    for j in range(rows_B):
        matrix_B.append([float(x) for x in input().split(" ")])
    #print(matrix_B)

    # Error check:
    if columns_A != rows_B:
        print("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        return

    # Calculate the resulting matrix (row by column)
    for i in range(rows_A):
        temp = []
        for j in range(columns_B):
            sum = 0
            for q in range(rows_B):
                sum += matrix_A[i][q] * matrix_B[q][j]
            temp.append(sum)
            #print(temp)
        matrix_C.append(temp)

        # Print out the resulting matrix
    #print(matrix_C)
    print("The result is:")
    for i in range(rows_A):
        for j in range(columns_B):
            print(matrix_C[i][j], end=" ")
        print("")
    print("")

def transpose_call():
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    choice = int(input("Your choice: "))

    matrix_A = []

    size_int_A = input("Enter matrix size: ")
    rows_A = int(size_int_A.split(" ")[0])
    columns_A = int(size_int_A.split(" ")[1])
    print("Enter matrix:")
    for j in range(rows_A):
        matrix_A.append([float(x) for x in input().split(" ")])

    # Get transposed matrix

    # Print out transposed matrix
    for i in range(rows_A):
        for j in range(columns_A):
            print(transpose(matrix_A, choice)[i][j], end=" ")
        print("")
    print("")

def transpose(matrix, choice):
    matrix_C = []
    rows = len(matrix)
    cols = len(matrix[0])
    # Get matrix_C the same size as input matrix_A
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(matrix)
        matrix_C.append(temp)

    # Check for choices
    if choice == 1:
        for i in range(rows):
            for j in range(cols):
                matrix_C[i][j] = matrix[j][i]
    elif choice == 2:
        for i in range(rows):
            for j in range(cols):
                matrix_C[i][j] = matrix[rows -1 -j][cols -1 -i]
    elif choice == 3:
        for i in range(rows):
            for j in range(cols):
                matrix_C[i][j] = matrix[i][cols -1 - j]
    elif choice == 4:
        for i in range(rows):
            for j in range(cols):
                matrix_C[i][j] = matrix[rows -1 -i][j]
    return matrix_C

def determinant_2_2(matrix):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

def determinant(matrix):
    #print(matrix)
    rows = len(matrix)
    cols = len(matrix[0])
    if rows == 1:
        return matrix[0][0]
    elif rows == 2:
        return determinant_2_2(matrix)
    else:
        # For every value in the top row
        deter = 0
        for i in range(rows):
            minor_matrix = []
            # Checking every value in the matrix (which are not in the first row or the corresponding column)
            for j in range(1, rows):
                row = []
                for q in range(cols):
                    if j != 0 and q != i:
                        row.append(matrix[j][q])
                minor_matrix.append(row)
            cofactor = determinant(minor_matrix)*(-1)**i
            deter += matrix[0][i]*cofactor
        return(deter)


def determinant_call():
    matrix_A = []

    size_int_A = input("Enter matrix size: ")
    rows_A = int(size_int_A.split(" ")[0])
    columns_A = int(size_int_A.split(" ")[1])
    print("Enter matrix:")
    for j in range(rows_A):
        matrix_A.append([float(x) for x in input().split(" ")])
    if rows_A != columns_A:
        return
    else:
        print(determinant(matrix_A))

def inverse(matrix):
    deter = determinant(matrix)
    transposed_matrix = transpose(matrix, 1)
    rows = len(transposed_matrix)
    cols = len(transposed_matrix[0])
    matrix_CT = []
    for i in range(rows):
        row_cofactors = []
        for j in range(cols):
            minor_matrix = []
            for q in range(rows):
                row =[]
                for p in range(cols):
                    if q != i and p != j:
                        row.append(transposed_matrix[q][p])
                if row != []:
                    minor_matrix.append(row)
            cofactor = determinant(minor_matrix)*((-1)**(i+j))
            row_cofactors.append(cofactor)
        matrix_CT.append(row_cofactors)
    inversed_matrix = []
    for i in range(rows):
        row_results = []
        for j in range(cols):
            row_results.append(matrix_CT[i][j] * 1/deter)
        inversed_matrix.append(row_results)
    return inversed_matrix

def inverse_call():
    matrix_A = []

    size_int_A = input("Enter matrix size: ")
    rows_A = int(size_int_A.split(" ")[0])
    columns_A = int(size_int_A.split(" ")[1])
    print("Enter matrix:")
    for j in range(rows_A):
        matrix_A.append([float(x) for x in input().split(" ")])
    if determinant(matrix_A) == 0:
        print("Determinant is zero!")
    else:
        inversed_A = inverse(matrix_A)
        for i in range(len(inversed_A)):
            for j in range(len(inversed_A[0])):
                print(f"{inversed_A[i][j]:.3f}", end=" ")
            print("")
        print("")

main()
