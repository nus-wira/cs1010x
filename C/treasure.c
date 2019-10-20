#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXSIZE 5

void scanArray(int [][MAXSIZE]);
int sumTreasures(int [][MAXSIZE], int, int, int, int);
int treasureHunt(int [][MAXSIZE], int, int*, int*, int*, int*);
int bestSum(int [][MAXSIZE], int, int, int, int*, int*);
int factors(int, int [][2]);

int main(void){
    int arr[MAXSIZE][MAXSIZE], size;
    int r1, c1, r2, c2, sum;
    scanArray(arr);
    scanf("%d", &size);

    sum = treasureHunt(arr, size, &r1, &c1, &r2, &c2);

    printf("sum:%d \nstart: %d %d\nend:%d %d",sum, r1, c1, r2, c2);
    return 0;

}

void scanArray(int arr[][MAXSIZE]){
    int i, j;

    for (i=0; i < MAXSIZE; i++){
        for (j=0; j < MAXSIZE; j++){
            scanf("%d", &arr[i][j]);
        }
    }
}

int sumTreasures(int arr[][MAXSIZE], int r1, int c1, int r2, int c2){
    int sum = 0, i, j;
    for(i = r1; i <= r2; i++){
        for (j=c1; j <= c2; j++){
            sum += arr[i][j];
        }
    }
    return sum;
}

int treasureHunt(int arr[][MAXSIZE], int size, int *r1, int *c1, int *r2, int *c2){
    int i,j, high_sum = 0, curr_sum, r2ptr, c2ptr;

    //check best area sum by each index
    for(i = 0; i < MAXSIZE; i++){
        for (j=0; j < MAXSIZE; j++){
            curr_sum = bestSum(arr, size, i, j, &r2ptr, &c2ptr);

            if (curr_sum > high_sum ){
                high_sum = curr_sum;
                *r1 = i;
                *c1 = j;
                *r2 = r2ptr;
                *c2 = c2ptr;
            }

        }
    }
    return high_sum;
}

//finds best sum of treasures given a fixed top left row and col index and inserts bottom right row and col index into pointers. returns the best sum.
int bestSum(int arr[][MAXSIZE], int size, int r1, int c1, int *r2, int *c2){
    int factorsArr[size][2];
    int nFactors = factors(size, factorsArr);
    int i, dr, dc, high_sum = 0, curr_sum;

    //for each pair of factors of size, find the rectangle area and replace high_sum if the sum is higher
    for (i = 0; i < nFactors; i++){
        //rectangle length across and length down respectively
        dr = factorsArr[i][0];
        dc = factorsArr[i][1];

        //if rectangle out of range skip
        if (r1+dr > MAXSIZE || c1+dc > MAXSIZE) continue;

        curr_sum = sumTreasures(arr, r1, c1, r1+dr-1, c1+dc-1);

        if  (curr_sum > high_sum){
            high_sum = curr_sum;

            *r2 = r1+dr-1;
            *c2 = c1+dc-1;

        }
    }
    return high_sum;
}

//finds factors of a number, inserts them into an array. returns number of pairs of factors.
int factors(int n, int arr[][2]){
    int i, count = 0;

    for (i=1; i <= n; i++){
        if (n%i == 0){

            arr[count][0] = i;
            arr[count][1] = n/i;
            count++;
        }
    }
    return count;
}
