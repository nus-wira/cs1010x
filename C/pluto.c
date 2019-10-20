#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void translate(char [], char []);

int main(void){
    printf("%d %d", 1/2 == 2/4, 1/3 == 0);
    /*
    char sentence[] = "i have a banana";
    char output[50] = {0};
    translate(sentence, output);
    printf("%s\n", output);
    */
    return 0;

}

void translate(char sentence[], char output[]){
    int count_a = 0, i = 0, j = 0, odd = 1;
    char wa[] = "wa ", fa[] = "fa ";
    while (sentence[i] != '\0'){
        if (sentence[i] == 'a' && !count_a){
            output[j] = 'o';
            count_a++;
        }
        else if (sentence[i] == ' '){
            output[j] = ' ';
            count_a = 0;
            if (odd)
                strcat(output, wa);
            else
                strcat(output, fa);
            odd = !odd;
            output[j+3] = ' ';
            j+=3;
        }
        else
            output[j] = sentence[i];
        i++;
        j++;
    }
    output[j] = ' ';
    if (odd)
        strcat(output, wa);
    else
        strcat(output, fa);
}
/*
//to add wa and fa
void addWord(char output[], int i, char c[]){
    int j;
    for (j = 0; j < 2; j++){
        output[i+j] = c[j];
    }

}
*/
