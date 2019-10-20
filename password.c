#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

void generate(char []);
void eightChar(char []);
char randomChar(char, char);

int main(void){

    char password[9]="";

    generate(password);

    printf("%s", password);

}
void generate(char password[]){
    srand(time(0));
    char s[9];
    int i, rand_i;
    char temp;

    //step 1
    eightChar(s);


    //step 2
    for (i = 0; i < 8; i++){
        rand_i = rand()%8;
        temp = s[i];
        s[i] = s[rand_i];
        s[rand_i] = temp;
    }

    strcpy(password, s);

}

char randomChar(char c1, char c2){

    return rand()%(c2-c1+1) + c1;
}

void eightChar(char s[]){
    int i;

    //lower case
    for(i= 0; i < 4; i++){
        s[i] = randomChar('a', 'z');
        //printf("%c\n", s[i]);
    }

    //upper case
    for (i; i < 6; i++){
        s[i] = randomChar('A','Z');
    }

    //upper case
    for (i; i < 8; i++){
        s[i] = randomChar('0','9');
    }

    s[8] = '\0';

}
