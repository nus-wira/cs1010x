#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void printArray(int [], int);
void maxPush(int [], int, int, int);
int maxPull(int [], int, int, int);

int main(void){
    int arr[] = {11, 3, 5, 8, 19, 7, 10, 12, 6, 9};
    int i = 6, d = 9, n = 10;
    maxPull(arr, n, i, d);
    printArray(arr, n);

    return 0;

}

void printArray(int arr[], int n){
    int i;
    for(i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
}


void maxPush(int arr[], int size, int index, int length){
    if (length == 1 || index + 1 == size) return;

    if (arr[index + 1] < arr[index])
        arr[index + 1] = arr[index];

    maxPush(arr, size, index + 1, length - 1);
}

int maxPull(int arr[], int size, int index, int length){
    if (length == 1 || index + 1 == size)
        return arr[index];

    int next_one = maxPull(arr, size, index + 1, length - 1);

    if (next_one > arr[index])
        arr[index] = next_one;

    return arr[index];
}
