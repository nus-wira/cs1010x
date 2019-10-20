#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SIZE 10

int determinant(int [][SIZE], int);
void get_mtx(int [][SIZE], int, int, int [][SIZE]);
void printArray(int arr[][SIZE], int n);

int main(void){
    int arr[5][SIZE] = {{1,2,3,4 ,5},{6, 7, 8, 9, 0}, {11, 12, 13, 13, 14}, {15, 16, 17, 18, 19},{20, 21, 22, 23, 24}};
    printf("%d\n", determinant(arr, 5));
    return 0;

}

void printArray(int arr[][SIZE], int n){
    int i, j;

    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int determinant(int mtx[][SIZE], int size){
    if (size == 2)
        return mtx[0][0]*mtx[1][1] - mtx[1][0]*mtx[0][1];

    int sum = 0, i, mul;
    int min_mtx[SIZE][SIZE];

    for (i = 0; i < size; i++){
        get_mtx(mtx, size, i, min_mtx);
        printArray(min_mtx, size -1);
        mul = i %2 ? -1 : 1;

        sum += mul * mtx[0][i] * determinant(min_mtx, size - 1);


    }
    return sum;
}

void get_mtx(int mtx[][SIZE], int size, int i, int min_mtx[][SIZE]){
    int r, c, c_min = 0;

    for (r = 1; r < size; r++){
        c_min = 0;
        for (c = 0; c < size; c++){
            if (c == i) continue;
            min_mtx[r-1][c_min++] = mtx[r][c];
        }
    }
}
