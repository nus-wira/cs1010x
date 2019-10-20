#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXROW 10

int scanGarden(int [][MAXROW]);
int maxTreasure(int [][MAXROW], int);
int genMaxTreasure(int [][MAXROW], int, int, int);


int main(void){
    int n;
    int arr[MAXROW][MAXROW];

    n = scanGarden(arr);

    printf("%d\n", maxTreasure(arr, n));

    return 0;

}

int scanGarden(int arr[][MAXROW]){
    int i, j, n;
    scanf("%d", &n);
    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    return n;
}
/*
3 1 6 2 4
1 9 8 2 2
6 9 1 1 3
4 1 5 1 2
2 4 6 2 1
*/

int maxTreasure(int arr[][MAXROW], int n){
    return genMaxTreasure(arr, n, 0, 0);
}

int genMaxTreasure(int arr[][MAXROW], int n, int r, int c){
    int curr_plot = arr[r][c];

    //at last plot
    if (r == n-1 && c == n-1)
        return curr_plot;
    // at bottom row
    else if (r == n - 1)
        return curr_plot + genMaxTreasure(arr, n, r, c+1);
    // at right most column
    else if (c == n - 1)
        return curr_plot + genMaxTreasure(arr, n, r+1, c);

    int path1, path2;

    path1 = genMaxTreasure(arr, n, r, c+1);
    path2 = genMaxTreasure(arr, n, r+1, c);

    if (path1 >= path2)
        return curr_plot + path1;
    else
        return curr_plot + path2;

}
