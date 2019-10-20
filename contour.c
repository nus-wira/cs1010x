#include <stdio.h>
#include <stdlib.h>
#define MAX_ROW 12
#define MAX_COL 12

void getPeaksValleys(int [][MAX_COL], int [][MAX_COL], int, int, int*, int*);
void getHikeTrail(int [][MAX_COL], int [][MAX_COL], int, int);
void scanArray(int [][MAX_COL], int, int);
void printArray(int [][MAX_COL], int, int);

int isPeakValley(int [][MAX_COL], int, int, int);
int isPeak(int [][MAX_COL], int, int);
int isValley(int [][MAX_COL], int, int);
void getReachable(int [][MAX_COL], int, int, int, int, int [][2]);
void markReachable(int [][MAX_COL], int [][MAX_COL], int, int, int, int);
void getAdjacent(int [][2], int, int, int, int);


int main(){
    int map[MAX_ROW][MAX_COL];
	int hike [MAX_ROW][MAX_COL] = {0};
	int peaksandvalleys [MAX_ROW][MAX_COL] = {};
	int nopeaks, novalleys;
	int row, col;

	printf("Enter no of rows and cols:");
	scanf("%d %d", &row, &col);
	printf ("Enter the data:\n");
	scanArray(map, row, col);

    getPeaksValleys(map, peaksandvalleys, row, col, &nopeaks, &novalleys);
    getHikeTrail(map, hike, row, col);

	return 0;
}

// function that reads in the data for the contour map
void scanArray(int array[][MAX_COL], int row, int col) {
	int r,c;
	for (r = 0; r < row; r++)
		for (c = 0; c < col; c++)
			scanf("%d", &array[r][c]);
}

// function that takes in and prints the 2D map
void printArray(int array[][MAX_COL], int row, int col) {
	int r,c;
	for (r = 0; r < row; r++) {
		for (c = 0; c < col; c++)
			printf("%d ", array[r][c]);
		printf("\n");
	}
}


void getPeaksValleys(int map[][MAX_COL],
                     int peaksandvalleys[][MAX_COL],
                     int row, int col,
                     int *nopeaks, int *novalleys){
    int i, j;
    *nopeaks = 0;
    *novalleys = 0;

    for (i = 1; i < row - 1; i++){
        for (j = 1; j < col - 1; j++){
            if (isPeak(map, i, j)){
                peaksandvalleys[i][j] = 1;
                (*nopeaks)++;
            } else if (isValley(map, i, j)){
                peaksandvalleys[i][j] = 2;
                (*novalleys)++;
            }
        }
    }
    printf("No of peaks: %d\n", *nopeaks);
    printf("No of valleys: %d\n", *novalleys);
    printf("Peaks and Valleys map\n");
    printArray(peaksandvalleys, row, col);

}

// checks whether a given row and column index is a peak/valley, depending on which it is checking for
int isPeakValley(int map[][MAX_COL], int row_i, int col_i, int checkPeak){
    int i, j, height = map[row_i][col_i], mul = 1;

    // if checking peak, no multiplier ( = 1), if valley, multiplier = - 1
    if (!checkPeak)
        mul = -1;

    for (i = -1; i < 2; i++){
        for (j = -1; j < 2; j++){
            if (i == 0 && j == 0) continue;
            // when mul = 1, this checks for peak (all surrounding are strictly greater)
            // when mul = -1, checks for valley
            // a >= b is equivalent to -a <= -b
            if (mul*height <= mul*map[row_i+i][col_i+j])
                return 0;
        }
    }
    return 1;
}

// uses isPeakValley function above to check for peak
int isPeak(int map[][MAX_COL], int row_i, int col_i){
    return isPeakValley(map, row_i, col_i, 1);
}

int isValley(int map[][MAX_COL], int row_i, int col_i){
    return isPeakValley(map, row_i, col_i, 0);
}

void getHikeTrail(int map[][MAX_COL], int hike[][MAX_COL], int row, int col){
    hike[0][0] = 1;
    markReachable(map, hike, row, col, 0, 0);
    printf("Hiking map\n");
    printArray(hike, row, col);
}

// takes in specific row & col index and marks in hike all reachable spots from there
void markReachable(int map[][MAX_COL], int hike[][MAX_COL], int row, int col, int row_i, int col_i){
    int reachArr[4][2] = {0}, do_next[4][2] = {0}, i, curr_row_i, curr_col_i, count = 0;

    // all reachable spots row and col index are inserted into an array reachArr
    getReachable(map, row, col, row_i, col_i, reachArr);

    // goes through each row,col pair in the reachArr array and changes hike[row][col] appropriately
    for (i = 0; i < 4; i++){
        curr_row_i = reachArr[i][0];
        curr_col_i = reachArr[i][1];
        // if no data in a row,col pair, skip
        if (curr_row_i == 0 && curr_col_i == 0) continue;

        /*
        if hike hasn't already been updated,
        1. update it
        2. keep track of how many updates are done from a single spot using count
        3. insert just updated row,col indexes into a do_next array
        if it has already been updated, it will automatically proceed to the next row,col pair
        */
        if (!hike[curr_row_i][curr_col_i]){
            hike[curr_row_i][curr_col_i] = 1;
            count++;
            do_next[i][0] = curr_row_i;
            do_next[i][1] = curr_col_i;
        }
    }
    /*
    if count == 0, it means that it went through the index without updating hike
    this means no more path to be updated from that point
    if no more path to mark stop
    */
    if (!count) return;

    // goes through each row,col pair in the do_next array and recursively uses this markReachable function
    // to mark the reachable spots from that spot
    for (i = 0; i < 4; i++){
        curr_row_i = do_next[i][0];
        curr_col_i = do_next[i][1];
        // only if have data, then proceed to mark
        if (curr_row_i || curr_col_i)
            markReachable(map, hike, row, col, curr_row_i, curr_col_i);
    }
}

// inserts all reachable spots from a spot into a reachArr array
void getReachable(int map[][MAX_COL], int row, int col, int row_i, int col_i, int reachArr[][2]){
    int adjArr[4][2] = {0}, i, curr_row_i, curr_col_i, curr_height, height = map[row_i][col_i];

    // inserts all adjacent spots from a spot into adjArr
    getAdjacent(adjArr, row, col, row_i, col_i);

    /*
    goes through each row,col pair in the adjArr array and checks for height difference
    between spot being checked and the spots around it
    */
    for (i = 0; i < 4; i++){
        curr_row_i = adjArr[i][0];
        curr_col_i = adjArr[i][1];
        // if no value skip
        if (curr_row_i == 0 && curr_col_i == 0) continue;

        curr_height = map[curr_row_i][curr_col_i];

        //if height diff <= 2, add reachable spot into the reachArr
        if (abs(curr_height - height) <= 2){
            reachArr[i][0] = curr_row_i;
            reachArr[i][1] = curr_col_i;
        }
    }

}

// inserts all 4 adjacent spots (up, down, left, right) into a adjArr array
void getAdjacent(int adjArr[][2], int row, int col, int row_i, int col_i){
    int i, rowChange, colChange, curr_row_i, curr_col_i;

    //for loop for all 4 spots
    for (i = 0; i < 4; i++){
        // default row/col change set to 0
        rowChange = 0;
        colChange = 0;
        //switch case to set the changes
        switch (i){
            case 0: // left
                colChange = -1;
                break;
            case 1: // right
                colChange = 1;
                break;
            case 2: // up
                rowChange = -1;
                break;
            case 3: // down
                rowChange = 1;
                break;
        }
        curr_row_i = row_i + rowChange;
        curr_col_i = col_i + colChange;
        // if out of range skip
        if (curr_row_i < 0 || curr_row_i >= row || curr_col_i < 0 || curr_col_i >= col) continue;

        // set row and col no in adjArr
        adjArr[i][0] = curr_row_i;
        adjArr[i][1] = curr_col_i;

    }
}


