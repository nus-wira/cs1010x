#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

#include <stdio.h>

int seesoo(long long);
int addDigits(long long);
int teetoo(long long);
int groupn(long long);
int modulo(long long, int);


int main(){
    printf("%d\n", seesoo(123456789012345678));
    printf("%d\n", teetoo(123456789012345678));
    printf("%d\n", seesoo(10020340567));
    printf("%d\n", teetoo(10020340567));

}

int seesoo(long long n){
    while (n > 9){
        n = addDigits(n);
    }
    return n;
}

int addDigits(long long n){
    int sum = 0;
    while (n > 0){
        sum += modulo(n, 10);
        n /= 10;
    }
    return sum;
}

int teetoo(long long n){
    int last_group = groupn(n);
    int sum;

    sum = modulo(n, last_group);
    n /= last_group * 10;

    while (n > 0){
        sum += modulo(n, 1000);
        n /= 10000;
    }

    return sum;

}

//Counts digits and returns 10^last group length
int groupn(long long n){
    int count = 0, res = 1, i;
    while (n > 0){
        count++;
        n /= 10;
    }
    count %= 4;
    for (i = 0; i < count; i++){
        res *= 10;
    }
    return res;
}

int modulo(long long n, int m){
    return n - (n/m)*m;
}

//only works for int inputs, and n >= 0
int pow_int(int x, int n){
    int i, res = 1;
    for(i = 0; i < n; i++){
        res *= x;
    }
    return res;
}
