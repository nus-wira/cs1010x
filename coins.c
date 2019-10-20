#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int count(int [], int, int);
void withoutFirst(int [], int [], int);


int main(void){
    int N = 10, m = 4;
    int S[] = {2,3,5,6};

    printf("%d\n", count(S, m, N));
    return 0;

}

int count(int S[], int m, int N){
    if (N == 0)
        return 1;
    if (m == 0 || N < 0)
        return 0;

    int restOfCoins[m], ways1, ways2;
    withoutFirst(S, restOfCoins, m);

    //with first coin
    ways1 = count(S, m, N - S[0]);
    //without first coin
    ways2 = count(restOfCoins, m - 1, N);

    return ways1 + ways2;
}

void withoutFirst(int S[], int restOfCoins[], int m){
    int i;
    for (i = 0; i < m-1; i++){
        restOfCoins[i] = S[i+1];
    }
}
