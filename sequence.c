/**
 * CS1010 AY2019/20 ST II Lab3 Ex2
 * Given a 12x12 integer array, fill it with integers, and
 * find the longest sequence of a digit that appears in
 * the array horizontally, vertically or diagonally.
 * R Ramana
 * Discussion Group 3
 */

#include <stdio.h>
#include <math.h>
#define DIM 12

// Fill in the function prototypes below
int scanBoard(int[][DIM]);
int search(int[][DIM], int, int*, int*);
int checkSeq(int[][DIM], int, int);
int maxAllRow(int[][DIM], int, int [], int);
int maxAllCol(int[][DIM], int, int []);
int maxAllDia(int[][DIM], int, int []);
int max1Row(int [], int, int*);
void translate(int[][DIM], int[][DIM]);
void transpose(int[][DIM], int[][DIM]);
int betterDir(int, int [], int, int []);


int main(void) {
	int board[DIM][DIM] = { {0} };
	int search_digit;
	int length;           // length of the longest sequence of search digit
	int bestRow, bestCol; // where the longest sequence of search digit starts in the board

	// call scanBoard()
    search_digit = scanBoard(board);
	// call search()
    length = search(board, search_digit, &bestRow, &bestCol);

	if (length > 0) {
		printf("Length of longest sequence = %d\n", length);
		printf("Start at (%d,%d)\n", bestRow, bestCol);
	}
	else
		printf("No such sequence.\n");

	return 0;
}

// Fill in the description of the function.
int scanBoard(int arr[][DIM]) {
    int r, c, searchDigit;

    for(r = 0; r < DIM; r++) {
        for(c = 0; c < DIM; c++) {
            scanf("%d", &arr[r][c]);
        }
    }

    scanf("%d", &searchDigit);

    return searchDigit;
}

// returns max possible sequence length and updates starting index of the sequence
int search(int arr[][DIM], int searchDigit, int *bestRow, int *bestCol){
    // variables to track indexes of best row, col & dia sequence lengths
    int row_ij[2], col_ij[2], dia_ij[2], dir; // direction variable for returning value later
    // variables to track best sequence lengths for each direction
    int row = maxAllRow(arr, searchDigit, row_ij, 0);
    int col = maxAllCol(arr, searchDigit, col_ij);
    int dia = maxAllDia(arr, searchDigit, dia_ij);

    // if no such digit return 0
    if (row == 0 && col == 0 && dia == 0) return 0;

    // find the best direction and make direction = to that direction
    if (betterDir(row, row_ij, col, col_ij)){
        if(betterDir(row, row_ij, dia, dia_ij))
            dir = 0;
        else
            dir = 2;
    } else {
        if(betterDir(col, col_ij, dia, dia_ij))
            dir = 1;
        else
            dir = 2;
    }

    // 0: row, 1: col, 2: dia
    switch (dir){
        case 0:
            *bestRow = row_ij[0];
            *bestCol = row_ij[1];
            return row;

        case 1:
            *bestRow = col_ij[0];
            *bestCol = col_ij[1];
            return col;
        case 2:
            *bestRow = dia_ij[0];
            *bestCol = dia_ij[1];
            return dia;
    }

}

//checks 2 directions with their indexes, returns the better direction (1 if the first one, 0 if the second one)
int betterDir(int dir1, int dir1_ij[], int dir2, int dir2_ij[]){
    // check for sequence length
    if (dir1 > dir2)
        return 1;
    else if (dir1 < dir2)
        return 0;

    //check for row index
    if (dir1_ij[0] < dir2_ij[0])
        return 1;
    else if (dir1_ij[0] > dir2_ij[0])
        return 0;

    //check for column index
    if (dir1_ij[1] < dir2_ij[1])
        return 1;
    else if (dir1_ij[1] > dir2_ij[1])
        return 0;

    //default first one
    return 1;
}

//finds the best sequence length of all rows and keeps track of the starting index of it
int maxAllRow(int arr[][DIM], int searchDigit, int row_ij[], int dir){
    int row_i, col_i, longest = 0, length, temp;

    //check row by row for best length
    for (row_i = 0; row_i < DIM; row_i++){
        //finds best length in a single row
        length = max1Row(arr[row_i], searchDigit, &col_i);
        if (length > longest){
            longest = length;
            row_ij[0] = row_i;
            row_ij[1] = col_i;
        }
    }

    //using input direction, edit row_ij to accurately reflect original array indexes
    // see translate and transpose functions below
    if (dir == 1){
        //since array is transposed {(i,j) -> (j,i)], indexes are swapped back
        temp = row_ij[0];
        row_ij[0] = row_ij[1];
        row_ij[1] = temp;
    } else if (dir == 2)
        row_ij[0] += row_ij[1] + 1 - DIM;


    return longest;
}

//finds best sequence length in a single row
int max1Row(int row[], int searchDigit, int *col_i){
    int curr_col_i, longest = 0, length, i;
    for (curr_col_i = 0; curr_col_i < DIM; curr_col_i++){

        //once we find a matching number
        if (row[curr_col_i] == searchDigit){
            length = 1;

            //for loop checks subsequent numbers if they are the same
            for (i = curr_col_i + 1; i < DIM; i++){
                if (row[i] == searchDigit)
                    length++;
                else
                    break;
            }
            //replace longest and column index input if longest in row
            if (length > longest){
                longest = length;
                *col_i = curr_col_i;
                curr_col_i = i + 1;
            }
        }
    }
    return longest;
}

int maxAllCol(int arr[][DIM], int searchDigit, int col_ij[]){
    //transpose array
    int t_arr[DIM][DIM];
    transpose(arr, t_arr);

    return maxAllRow(t_arr, searchDigit, col_ij, 1);
}

int maxAllDia(int arr[][DIM], int searchDigit, int dia_ij[]){
    //translate array
    int t_arr[DIM+DIM][DIM] = {0};
    translate(arr, t_arr);

    return maxAllRow(t_arr, searchDigit, dia_ij, 2);
}


/*
transposes array and inserts into a t_arr
transpose it so that maxAllRow fn above can be used for columns
transpose:
1 2 3     1 4 7
4 5 6 --> 2 5 8
7 8 9     3 6 9

*/
void transpose(int arr[][DIM], int t_arr[][DIM]){
    int i, j;

    for (i = 0; i < DIM; i++){
        for (j = 0; j < DIM; j++){
            t_arr[i][j] = arr[j][i];
        }
    }
}


/*
translates array such that diagonals (going down_right) become rows
translating it so that maxAllRow fn above can be used for diagonals
translate:
1 2 3     0 0 3
4 5 6 --> 0 2 6
7 8 9     1 5 9
          4 8 0
          7 0 0
*/
void translate(int arr[][DIM], int t_arr[][DIM]){
    int i, j;

    for (i = 0; i < DIM; i++){
        for (j = 0; j < DIM; j++){
            t_arr[i+DIM-j-1][j] = arr[i][j];
        }
    }
}
