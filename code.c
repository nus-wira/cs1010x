#include <math.h>
#include <stdio.h>

#define MIN_HOUR 60
#define HOUR_DAY 24

void gameCode(int, int, int);
int toMinutes(int, int, int);
int toTwoDigit(int);
char codeChar(int);
int root(int);

int main(){
    gameCode(1, 2, 3);

    return 0;

}

void gameCode(int day, int hr, int min){
    char c1, c2;
    int twoDigit = toTwoDigit(toMinutes(day, hr, min));

    c1 = codeChar(twoDigit);
    c2 = codeChar(root(twoDigit));
    printf("%c%c",c1,c2);
}

int toMinutes(int day, int hr, int min){
    return HOUR_DAY*MIN_HOUR*day + MIN_HOUR*hr + min;
}

int toTwoDigit(int n){
    int dgt1 = n /1000, dgt2 = n %10;
    return dgt1*10 + dgt2;
}

char codeChar(int n){
    if (n % 2 == 0)
        return 'A';
    else if (n % 3 == 0)
        return 'F';
    else if (n % 5 == 0)
        return 'K';
    else if (n % 7 == 0)
        return 'P';
    else if (n % 11 == 0 || n % 13 == 0)
        return 'T';
    else
        return 'Z';
}

int root(int n){
    return (int)(sqrt(n)*100) % 100;
}
