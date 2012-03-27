#THREE GOLD STARS

#Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#is a logic puzzle where a game
#is defined by a partially filled
#9 x 9 square of digits where each square
#contains one of the digits 1,2,3,4,5,6,7,8,9.
#For this question we will generalize
#and simplify the game.


#Define a procedure, check_sudoku,
#that takes as input a square list
#of lists representing an n x n
#sudoku puzzle solution and returns
#True if the input is a valid
#sudoku square and returns False
#otherwise.

#A valid sudoku square satisfies these
#two properties:

#   1. Each column of the square contains
#       each of the numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]


def check_sudoku(inputlist):
    n = len(inputlist[0]);
    #check row and column to make sure they sum to (n+1)(n)/2
    
    #check row first
    rowsum = 0;
    for e in inputlist:
        for ele in e:
            rowsum = rowsum + ele;
        if (rowsum != (n+1)*n/2):
            return False;
        rowsum = 0;
    
    #now check column
    colsum = 0;
    integer = 0;
    integer2 = 0;
    while (integer < n):
        while (integer2 < n):
            colsum = colsum + inputlist[integer2][integer];
            print colsum;
            integer2 = integer2 + 1;
        if (colsum != (n+1)*n/2):
            return False;
        colsum = 0;
        integer2 = 0;
        integer = integer + 1;
    
    #now check for repeats
    for e in inputlist:
        count = 0;
        while (count < n):
            if e.count(count+1) != 1:
                return False;
            count = count + 1;

    #otherwise return true
    return True;
            
print check_sudoku(correct)
