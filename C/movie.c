#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_MOVIES 100

void scanArray(int [][MAX_MOVIES], int, int);
void mostSimilar(int [][MAX_MOVIES], int, int, int*, int*);
int dist(int [][MAX_MOVIES], int, int, int);


int main(void){
    printf("%d", '0');
    /*
    int m_par = 4, n_mov = 5;
    int arr[m_par][MAX_MOVIES];
    int p1, p2;

    scanArray(arr, n_mov, m_par);

    mostSimilar(arr, n_mov, m_par, &p1, &p2);

    printf("Winners: %d %d\n", p1, p2);
    */
}

void scanArray(int arr[][MAX_MOVIES], int n_mov, int m_par){
    int i, j;

    for (i=0; i < m_par; i++){
        for (j=0; j < n_mov; j++){
            scanf("%d", &arr[i][j]);
        }
    }
}

void mostSimilar(int arr[][MAX_MOVIES], int n_mov, int m_par, int *p1, int *p2){
    int distance = dist(arr, n_mov, 0, 1), curr_dist, i, j;

    for (i = 0; i < m_par; i++){
        for (j = i+1; j < m_par; j++){
            curr_dist = dist(arr, n_mov, i, j);
            if (curr_dist < distance){
                distance = curr_dist;
                *p1 = i;
                *p2 = j;
            }
        }
    }

}

int dist(int arr[][MAX_MOVIES], int n_mov, int p1, int p2){
    int sum = 0, i, rate1, rate2;

    for (i = 0; i < n_mov; i++){
        rate1 = arr[p1][i];
        rate2 = arr[p2][i];
        sum += (rate1 - rate2)*(rate1 - rate2);
    }

    return sqrt(sum);
}
