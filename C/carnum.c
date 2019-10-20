#include <stdio.h>

#define MAX_LENGTH 8

int isValidChecksum(char []);
char genChecksum(char []);
int isValidLetters(char []);
int isVowel(char);
void getCarType(char []);
int getNum(char []);
char getCheckChar(char []);
int letterToNum(char);
//functions to check if a char is a digit/letter
int my_isalpha(char);
int my_isdigit(char);
int my_isalnum(char);



int main(void) {
	char regNo[MAX_LENGTH + 1];

	printf("Enter car reg no: ");
	scanf("%s", regNo);

	if (isValidChecksum(regNo))
        printf("Valid registration number\n");
    else
        printf("Invalid registration number\n");

	return 0;
}

// A function that takes in the registration number string, and returns 1 if the registration number is valid, or 0 otherwise.
int isValidChecksum(char regNo[]) {
    // if invalid character in first 7 chars
    if (!isValidLetters(regNo) || !getNum(regNo))
        return 0;

    getCarType(regNo);

    return genChecksum(regNo) == getCheckChar(regNo);
}

// Checks first 3 letters of regNo
int isValidLetters(char regNo[]){
    return regNo[0] == 'S' && my_isalpha(regNo[1]) && !isVowel(regNo[1]) && my_isalpha(regNo[2]);
}

int isVowel(char c){
    int i = 0;
    char s[] = "AEIOU";
    for (i; i < 5; i++){
        if (c == s[i])
            return 1;
    }
    return 0;
}

// Retrieves number from regNo
int getNum(char regNo[]){
    int i = 3, num = 0, digit;
    char c;

    //if 4th char in the regNo is a letter false
    if (!my_isdigit(regNo[3]))
        return 0;

    for (i; i < MAX_LENGTH - 1; i++){
        c = regNo[i];
        if (my_isdigit(c)){
            digit = c - '0';
            num *= 10;
            num += digit;
        } else if (my_isalpha(c))
            break;
        else
            return 0; //invalid character
    }

    return num;
}

// Prints corresponding cartype
void getCarType(char regNo[]) {
	char arr[] = "HZG", c = regNo[1];
	int i = 0;
	for (i; i < 3; i++){
        if (c == arr[i]) break;
	}
	printf("Car is a ");
    switch (i){
        case 0:
            printf("taxi\n");
            break;
        case 1:
            printf("rental car\n");
            break;
        case 2:
            printf("goods vehicle\n");
            break;
        case 3:
            printf("private car\n");
            break;
    }
}

// Returns correct char checksum for regNo
char genChecksum(char regNo[]) {
    // array to store the 6 numbers used
	int arr[6] = {0}, mul[] = {9, 4, 5, 4, 3, 2};
	int i, num = getNum(regNo), res = 0;
	// char array to check which number checksum corresponds to which char
	char checksum[] = "AZYXUTSRPMLKJHGEDCB";

    // getting the 6 numbers used into the array arr
	//getting the 2 letters NX1 NX2
	for (i = 0; i < 2; i++){
        arr[i] = letterToNum(regNo[i+1]);
	}
	//getting the 4 numbers X1 to X4
	i = 5;
	while (num > 0) {
        arr[i--] = num % 10;

        num /= 10;
	}

	//finding the product and subsequent sum
	for (i = 0; i < 6; i++){
        arr[i] *= mul[i];
        res += arr[i];

	}

	res %= 19;

	//cross-references with char checksum array above and returns correct char
	for (i = 0; i < 19; i++){
        if (res == i)
            return checksum[i];
	}

}

// converts letter to number A = 1, B = 2, ..., Z = 26
int letterToNum(char c){
    int i;
    char s[] = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (i = 1; i < 26; i++){
        if (c == s[i])
            return i;
    }
}

// Gets the checksum char used in the input regNo
char getCheckChar(char regNo[]){
    int i;
    char c;
    for (i = 4; i < MAX_LENGTH; i++){
        c = regNo[i];
        if (my_isalpha(c)){
            //if extra characters then false
            if (i < MAX_LENGTH && regNo[i+1] != '\0')
                return 0;
            return c;
        }

    }

}

// Functions check for letters/numbers
int my_isalpha(char c){
    int i = 0;
    char s[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (i; i < 26; i++){
        if (c == s[i])
            return 1;
    }
    return 0;
}

int my_isdigit(char c){
    int i = 0;
    char s[] = "0123456789";
    for (i; i < 10; i++){
        if (c == s[i])
            return 1;
    }
    return 0;
}

int my_isalnum(char c){
    return my_isalpha(c) || my_isdigit(c);
}
