#include <math.h>
#include <stdio.h>


void maxswap(int [], int, int);
int findMax(int [], int, int, int);
void moveToIndex(int [], int, int);
void printArray(int [], int);

int main(){
    int size = 8;
    int i;
    int arr[] = {9, 5, 9, 2, 2, 4, 7, 9};
    int nswaps = 15;

    maxswap(arr, size, nswaps);

    printArray(arr, size);

    return 0;

}

void printArray(int arr[], int size){
    int i;
    for (i = 0; i < size; i++){
        printf("%d", arr[i]);

    }
    printf("\n");
}

/*
Max number can be determined iteratively.
1. Check the highest number within the indexes from 0 to numswap
2. Obtain the index of the highest number, and move it to the start (index 0) using neighbour swaps
3. Take numswap = numswap - index
4. Repeat steps 1 to 3, but your index 0 has moved 1 forward
*/


void maxswap(int arr[], int size, int numswap){
    int max_i, i = 0;

    while (numswap > 0 && i < size){
        max_i = findMax(arr, i, numswap, size);

        moveToIndex(arr, i, max_i);

        //max_i - i equals to the no. of swaps in a single loop
        numswap -= max_i - i++;

    }
}

// finds max index from start_i to start_i + numswap and returns the index of max
int findMax(int arr[], int start_i, int numswap, int size){
    int i, high = arr[start_i], high_i = start_i, num;
    for (i = start_i + 1; i <= start_i + numswap && i < size; i++){
        num = arr[i];
        if (num > high){
            high = num;
            high_i = i;
        }
    }
    return high_i;
}

// moves a highest number from max_i to start_i using neighbour swaps
void moveToIndex(int arr[], int start_i, int max_i){
    int i, temp;
    for (i = max_i; i > start_i; i--){
        temp = arr[i-1];
        arr[i-1] = arr[i];
        arr[i] = temp;
    }
}
