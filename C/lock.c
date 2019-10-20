#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LETTERS 26

int match(char [], char []);
void nLettersStr(int [], char []);
void nLettersPat(int [], char []);

int main(void){

    if (match("CAAAAEEEK","3E4A1K"))
        printf("YES");
    else
        printf("NO");
    return 0;


}

int match(char str[], char pat[]){
    int i, strLetterArr[LETTERS] = {0}, patLetterArr[LETTERS] = {0};

    nLettersStr(strLetterArr, str);
    nLettersPat(patLetterArr, pat);

    for (i = 0; i < LETTERS; i++){
        if (strLetterArr[i] != patLetterArr[i])
            return 0;
    }
    return 1;
}

void nLettersPat(int arr[], char pat[]){
    int i = 0, chr_index, dgt;
    while (pat[i] != '\0'){
        dgt = pat[i] - '0';
        chr_index = pat[i+1] - 'A';
        arr[chr_index] = dgt;
        i += 2;
    }
}

void nLettersStr(int arr[], char str[]){
    int i = 0, chr_index;
    while (str[i] != '\0'){
        chr_index = str[i++] - 'A';
        arr[chr_index]++;
    }
}
