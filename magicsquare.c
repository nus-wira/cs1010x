#include <math.h>
#include <stdio.h>

#define MAX_SIZE 9

int main(){


    return 0;

}


int checkNum(int arr[][MAX_SIZE], int size){
    int r, c, num_arr[size*size] = {0}, num;

    for (r = 0; r < size; r++){
        for (c = 0; c < size; c++){
            num = arr[r][c];

            if (num < 1 || num > size*size || num_arr[num-1] != 0)
                return 0;
            else
                num_arr[num-1]++;
        }
    }

    return 1;
}
