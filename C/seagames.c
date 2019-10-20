#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
 char sport[21]; // Name of the sport
 char type; // Type of the medal: 'G' = gold,
 // 'S' = silver and 'B' = bronze.
} medal_t;
typedef struct {
 char code[4]; // Code name of the country
 int numMedals; // Number of medals
 medal_t medals[201]; // Medals won by the country
} country_t;

int readResults(country_t []);
void sortCountries(country_t [], int);
void findWinners(country_t [], int , char [], char []);

int main(void){
    /*
    country_t countries[200];
    int i, n;
    char winners[15];
    n =readResults(countries);
    sortCountries(countries, n);
    findWinners(countries, n, "Marathon", winners);
    for (i = 0; i < 1; i++){
        printf("%s %d\n%s %c\n", countries[i].code, countries[i].numMedals, countries[i].medals[i].sport,countries[i].medals[i].type);
    }
    printf("%s", winners);
    */
    char *str1 = "app", *str2 = "pineapple";
    char *str3 = strstr(str2, str1), str4[12]="pine";
    strcat(str4, str3);
    printf("%s", str4);

    return 0;
}

int readResults(country_t countries[]){
    char sport[21], type, code[4],  medal;
    int numMedals, i, nCountries, j;
    FILE *fptr;
    if ((fptr = fopen("medals.txt", "r")) == NULL)
    {
        printf("Error! opening file");
        // Program exits if file pointer returns NULL.
        exit(1);
    }

    fscanf(fptr, "%d", &nCountries);
    for (i = 0; i < nCountries; i++){
        fscanf(fptr, "%s %d", &code, &numMedals);
        strcpy(countries[i].code , code);
        countries[i].numMedals = numMedals;
        for (j = 0; j < numMedals; j++){
            fscanf(fptr, "%s %c", &sport, &type);
            strcpy(countries[i].medals[j].sport,sport);
            countries[i].medals[j].type = type;

        }
    }
    fclose(fptr);

    return nCountries;
}

void sortCountries(country_t countries[], int num){
    int i, j;
    country_t temp;
    //bubble sort
    for (i = 0; i < num - 1; i++){
        for (j = 0; j < num - 1 - i; j++){
            if (countries[j].numMedals < countries[j+1].numMedals){
                temp = countries[j];
                countries[j] = countries[j+1];
                countries[j+1] = temp;
            }
        }
    }
}

void findWinners(country_t countries[], int num, char sport[], char winners[])  {
    int i, numMedals, j, count = 0;
    medal_t medals;
    char type, arr[3][4], *ptr;

    for (i = 0; i < num; i++){
        numMedals = countries[i].numMedals;

        for (j = 0; j <numMedals; j++){
            medals = countries[i].medals[j];

            // if sport medal matches given sport
            if (!strcmp(medals.sport, sport)){
                type = medals.type;
                //switch case sets the pointer to the right place in winners
                switch(type){
                    case 'G':
                        ptr = winners;
                        break;
                    case 'S':
                        ptr = &winners[4];
                        break;
                    case 'B':
                        ptr = &winners[8];
                        break;
                }
                strcpy(ptr, countries[i].code);
            }
        }
    }
    winners[3] = '*';
    winners[7] = '*';
}

/*
void findWinners(country_t countries[], int num, char sport[], char winners[])  {
    int i, numMedals, j, count = 0;
    medal_t medals;
    char type, arr[3][4];


    for (i = 0; i < num; i++){
        numMedals = countries[i].numMedals;

        for (j = 0; j <numMedals; j++){
            medals = countries[i].medals[j];

            if (!strcmp(medals.sport, sport)){
                type = medals.type;
                switch(type){
                    case 'G':
                        strcpy(arr[0], countries[i].code);
                        break;
                    case 'S':
                        strcpy(arr[1], countries[i].code);
                        break;
                    case 'B':
                        strcpy(arr[2], countries[i].code);
                        break;
                }
            }
        }
    }
    for (i = 0; i < 3; i++){
        strcat(winners, arr[i]);
        if (i < 2)
            strcat(winners, "*");
    }
}
*/
