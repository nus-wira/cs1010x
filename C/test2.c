// CS1010 AY2015/6 Semester 1
// PE2 Ex1: panel.c
// Name:
// Matriculation number:
// plab-id:
// Discussion group:
// Description:

#include <stdio.h>

int multiply2Digit(int);
void giveAdvice(int, int);
int multiplyOnce(int);


int main(void) {
    int num;
    printf("Enter a non-zero integer: ");
    scanf("%d", &num);

    giveAdvice(multiply2Digit(abs(num)), num > 0);

    return 0;
}

int multiply2Digit(int n){
    while (n > 9){
        n = multiplyOnce(n);
    }
    return n;
}

int multiplyOnce(int n){
    int res = 1;
    while (n > 0){
        res *= (n%10);
        n /= 10;
    }
    return res;
}

void giveAdvice(int dgt, int sign){
    if (sign){
        switch (dgt){
            case 0:
            case 3:
            case 7:
            case 9:
                printf("You should protect life.\n");
                break;
            case 2:
            case 5:
            case 8:
                printf("Share your wealth, donate generously.\n");
                break;
            case 1:
            case 4:
            case 6:
                printf("Build harmony, bring people together.\n");
                break;
        }
    } else {
        switch (dgt){
            case 0:
            case 3:
            case 7:
            case 9:
                printf("Speak honestly.\n");
                break;
            case 2:
            case 5:
            case 8:
                printf("Praise others' successes.\n");
                break;
            case 1:
            case 4:
            case 6:
                printf("Lend your hand to those who are in need.\n");
                break;
        }
    }
}
