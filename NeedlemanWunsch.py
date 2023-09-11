import numpy as np
#commit 1
# amend local


def print_mat(mat, seqA, seqB):

    print("\t\t\t\t", end="")
    for char in seqA:
        print(char, end="\t\t\t\t")
    print()

    for row_index in range(len(seqB)+1):
        # TODO: This conditional clause gets executed only once. Can we
        #  improve this?
        if(row_index < 1):
            print(" ", end=" ")
        else:
            print(seqB[row_index-1], end=" ")
        for col in mat[row_index]:
            # TODO: How do I vertically align text output?
            print(col, end="\t")
            # print('%-20s %i' % col)
        print()


def needleman_wunsch(seqA, seqB):
    def fill_mat_row(mat, seq_a, seq_b, row):
        print("bruh")

    def fill_mat_col(mat, seq_a, seq_b, col):
        print("bruh")

    mat = [[(0, 0, 0, 0) for _ in range(len(seqA) + 1)] for _ in
           range(
               len(seqB) + 1)]

    # Initialize the first row and col of the matrix
    count = 0
    for col in range(len(mat[0])):
        mat[0][col] = (count, 0, 0, 0)
        count -= 2
    count = 0
    for row in range(len(mat)):
        mat[row][0] = (count, 0, 0, 0)
        count -= 2

    print_mat(mat, seqA, seqB)

    #Fill out the rest of the matrix!


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    seqA = 'DUCK'
    seqB = 'TRUMP'
    needleman_wunsch(seqA, seqB)
