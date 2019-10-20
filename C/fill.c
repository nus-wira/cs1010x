#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void printArray(int [][20], int);
void fill (int [][20], int);


int main(void){
    int arr[20][20];
    int n = 6;
    fill(arr, n);
    printArray(arr, n);
    return 0;

}

void printArray(int arr[][20], int n){
    int i, j;

    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

void fill(int arr[][20], int n) {
    int i, j;

    for(i=0;i<n;i++) {
        for(j=0;j<n;j++) {
            arr[i][n-1] = n;
            arr[n-1][j] = n;
        }
    }

    if(n != 1) {
        fill(arr, n-1);
    }

}
/*

void fill(int arr[][20], int n){
    if (n == 1){
        arr[0][0] = 1;
        return;
    }

    int i;

    for (i = 0; i < n; i++){
        arr[i][n-1] = n;
        arr[n-1][i] = n;
    }

    fill(arr, n-1);
}*/
