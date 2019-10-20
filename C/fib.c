#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void printArray(int [][20], int);
void fill (int [][20], int);

int fib_it(int);
int main(void){
    printf("%d\n", fib_it(5));
    printf("%d\n", fib_rec(5));

}

int fib_it(int n){
    int i, a = 0, b = 1, temp;

    for (i = 1; i < n; i++){
        temp = b;
        b += a;
        a = temp;
    }
    return b;
}

int fib_rec(int n){
    if (n == 1 || n == 0) return n;
    return fib_rec(n-1) + fib_rec(n-2);
}
