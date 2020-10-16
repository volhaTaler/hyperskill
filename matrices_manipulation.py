from copy import copy, deepcopy

def print_actions():
    print("""1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
    0. Exit""")

def exit():
    return False

def choose_transpose():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    return input()

# this fuction returns number of rows and columns of the input matrix

def params(matrix):
    return len(matrix), len(matrix[0])
    
# returns an empty matrix for transpose operation
def transposed_muster(col):
    matrix = []
    for i in range(col):
        matrix.append([])
    return matrix
    
# transpose 1
def main_diagonal(matrix):
    n, m = params(matrix)
    mtr = transposed_muster(m) 
    for row in matrix:
        for i in range(m):
            mtr[i].append(row[i]) 
    return mtr 

# transpose 2
def side_diagonal(matrix):
    n, m = params(matrix)
    mtr = transposed_muster(m)    
    for row in matrix:
        row = row[::-1]
        for i, cell in enumerate(row):
            mtr[i].insert(0,cell) 
    return mtr

# transpose 3
def vertical_line(matrix):
    n, m = params(matrix)
    mtr = []    
    for row in matrix:
        row = row[::-1]
        mtr.append(row)
    return mtr

# transpose 4
def horizontal_line(matrix):
    n, m = params(matrix)
    mtr = []    
    for row in matrix:
            mtr.insert(0,row)
    return mtr

# returns a row with max number of zeros for determenant calculation
def find_zero_row(matrix):
    count =[]
    for row in matrix:
        count.append(row.count(0))
    return count.index(max(count))

# calculation of determenant for 2x2 matrix
def calc_2d_det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

# returns matrix with changed signes for cofactors.
# The signs are changed only for the row used for determenant calcuation    
def correct_sign(matrix, row_num):
    for  i in range(len(matrix[0])):
            check_number = i + row_num
            if check_number % 2 == 1:
                matrix[row_num][i] *= -1
    return matrix
    
# returns cofactor matrix for inverse matrix
def cofactors_matrix(matrix):
    n, m = params(matrix)
    for i in range(n):
        matrix = correct_sign(matrix, i)
    return matrix

# calculation of determenant for nxn matrices with n > 2.
def calc_determinant(matrix):
    n, m = params(matrix)
    if n == m == 2:
        return calc_2d_det(matrix)
    elif n == m == 1:
        return matrix[0][0]
    elif n != m:
        print("Something went wrong! Matrix is not square!")
    else:
        # check if there are any rows with zeros
        row_id = find_zero_row(matrix)
        # define a correct sign
        matrix = correct_sign(matrix, row_id)
        matrices = []  
        for k in range(m):
            mtr = []
            for i in range(n):
                if i != row_id:
                    row = []
                    if k == m - 1:
                        row = matrix[i][:-1]
                    else:
                        row = matrix[i][:k] + matrix[i][k + 1:]
                    mtr.append(row)
            if matrix[row_id][k] == 0:
                matrices.append(0)
            else:
                matrices.append(calc_determinant(mtr) * matrix[row_id][k])
        return sum(matrices)

# returns swapped matrix for inverse 2x2 matrix
def swap_matrix(matrix):
    tmp = matrix[0][0]
    matrix[0][0] = matrix[1][1]
    matrix[1][1] = tmp
    matrix[0][1] *= -1
    matrix[1][0] *= -1
    return matrix
    
# returns a matrix of minors for nxn inverse matrix with n > 2
def find_minors(matrix):
    n, m = params(matrix)
    minor_m = []
    for ignore_r in range(n):
        minor_row = []
        for ignore_c in range(n):
            det_m = []
            for i in range(n):
                row = []
                if i == ignore_r:
                    pass    
                else: 
                    if ignore_c == n - 1:
                        row = matrix[i][:-1]
                        
                    else:
                        row = matrix[i][:ignore_c] + matrix[i][ignore_c + 1:]
                    det_m.append(row)
            minor_row.append(calc_determinant(det_m))         
        minor_m.append(minor_row)
    return minor_m

# this function converts 0.0 or -0.0 to 0
# this improvement ia needed to pass tests in jetbrains platform.
def improve(matrix):
    n, m = params(matrix)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 0
    return matrix

# calculate inverse matrix    
def inverse_matrix(matrix):
        mtr = deepcopy(matrix)
        det = calc_determinant(mtr)
        if det == 0:
            print("This matrix doesn't have an inverse.")
            return None
        else:
            n, m = params(matrix)
            scalar = float(1 / det) 
            if  n == 1:
                return scalar * matrix[0][0]
            elif n == 2:
                matrix = swap_matrix(matrix)
                return scalar_multipilcation(matrix, scalar)
            elif n > 2:
                matrix = find_minors(matrix)
                matrix = cofactors_matrix(matrix)
                matrix = main_diagonal(matrix)
                mtr = scalar_multipilcation(matrix, scalar)
                mtr = improve(mtr)
                return mtr

def proceed_transpose():
    num = choose_transpose()
    n, m = input("Enter size of matrix:").split()
    print("Enter matrix:")
    matrix = creat_matrix(int(n), int(m))
    if num == "1":
        print_result(main_diagonal(matrix))
    elif num == "2":
        print_result(side_diagonal(matrix))
    elif num == "3":
        print_result(vertical_line(matrix))
    elif num == "4":
        print_result(horizontal_line(matrix))

# this function creates two matrices from user's input.
def two_matrices():
    n, m = input("Enter size of first matrix:").split()
    print("Enter first matrix:")
    m1 = creat_matrix(int(n), int(m))
    n2, m2 = input("Enter size of second matrix:").split()
    m2 = creat_matrix(int(n2), int(m2))
    return m1, m2

# this function asks user to enter a matrix.   
def enter_matrix():
    n, m = input("Enter size of matrix:").split()
    print("Enter matrix:")
    return creat_matrix(int(n), int(m)), n, m

# working loop will be executed untill the user chooses "exit" option.
def perform():
    execution = True
    while execution:
        print_actions()
        choice = input("Your choice: ")
        if choice == "1":
            m1, m2 = two_matrices()
            if len(m1) != len(m2) or len(m2[0]) != len(m1[0]):
                print("The operation cannot be performed.")
            else:
                print_result(add_matrices(m1, m2))
        elif choice == "2":
            m1, _, _ = enter_matrix()
            const = cast_(input("Enter constant:"))
            print_result(scalar_multipilcation(m1, const))
        elif choice == "3":
            m1, m2 = two_matrices()
            if len(m1[0]) == len(m2):
                print_result(multiply_matrices(m1, m2))
            else:
                print("The operation cannot be performed.") 
        elif choice == "4":
            proceed_transpose()
        elif choice == "5":
            matrix, n, m = enter_matrix()
            if n != m:
                print("A determinant can be calculated for square matrix only! Please check your input data.")
            else:
                print("The result is:")
                print(calc_determinant(matrix))
        elif choice == "6":
            matrix, n, m = enter_matrix()
            
            print_result(inverse_matrix(matrix))
        elif choice == "0":
            execution = exit() 

# cotvert input string elements to integer or to float.                       
def cast_(scalar):
    if "." in scalar:
        return float(scalar)
    else:
        return int(scalar)

# returns a matrix from user's input
def creat_matrix(n, m):
    matrix = []
    for i in range(n):
        row_i = []
        row = input().split()
        for j in range(m):
            row_i.append(cast_(row[j]))
        matrix.append(row_i) 
    return matrix

# addition of matrices
def add_matrices(m1, m2):
    n, m = params(m1)
    for i in range(n):
        for j in range(m):
            m1[i][j] += m2[i][j]
    return m1

def print_result(matrix):
    if matrix is not None:
        print("The result is:")
        n, m = params(matrix)
       # print()
        for i in range(n):
            row = ""
            for j in range(m):
                row += str(matrix[i][j]) + " "
            print(row)
        print()
    else:
        print("There is no result!")

def scalar_multipilcation(matrix, scalar):
    n, m = params(matrix)
    for i in range(n):
        for j in range(m):
            matrix[i][j] = scalar * matrix[i][j]
    return matrix
    
def multiply_matrices(m1, m2):
    n, s = params(m1)
    m = len(m2[0])
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            item = 0
            for k in range(s):
                item += m1[i][k] * m2[k][j]
            row.append(item)
        matrix.append(row)
    return matrix
  
perform()  