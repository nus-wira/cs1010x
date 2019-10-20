#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <math.h>

#define DOMAIN_NAME "u.nus.edu"


int checkEmail(char []);
int separate(char [], int, char [], char);
int checkValid(char [], char [], int);
int checkFriendly(char []);


int main(){
    char email[50];
    int checked;

    printf("Enter email address: ");
    scanf("%s", email);
    checked = checkEmail(email);
    printf("This email address is ");

    if (!checked)
        printf("not valid.");
    else if (checked == 1)
        printf("valid but not friendly.");
    else
        printf("valid and friendly.");

    return 0;
}

// Checks validity and friendliness of email
int checkEmail(char email[]){
    int local_len, domain_len;
    char local[25] = "";
    char domain[25] = "";
    char c = '@';

    local_len = separate(email, 0, local, c);
    domain_len = separate(email, local_len + 1, domain, '\0') - local_len - 1;

    if (!checkValid(local, domain, local_len))
        return 0;
    else if (local_len > 8 || checkFriendly(local))
        return 2;
    else
        return 1;

}

// Separates email into relevant input part, returns ending index
int separate(char email[], int i, char part[], char c){
    int j = 0;
    while (email[i] != c){
        part[j++] = email[i++];
    }
    return i;
}

int checkValid(char local[], char domain[], int local_len){
    int i;

    int validLength = local_len > 2 && local_len < 22;
    int validDomain = !strcmp(domain, DOMAIN_NAME);
    int validLocal = 1;
    if (!isalpha(local[0]))
        validLocal = 0;
    else {
        for (i = 1; i < local_len; i++){
            if (!isalnum(local[i]) && local[i] != '.'){
                validLocal = 0;
                break;
            }
        }
    }
    return validLength && validLocal && validDomain;
}

// checks whether
int checkFriendly(char local[]){
    int i = 1;

    if (local[0] == 'a' || local[0] == 'e'){
        for (i; i < 8; i++){
            if (!isdigit(local[i]))
                return 1;
        }
    }
    return 0;
}
/*
int isalpha(char c){
    int i = 0;
    char s[] = "abcdefghijklmnopqrstuvwxyz";
    for (i; i < 26; i++){
        if (c == s[i])
            return 1;
    }
    return 0;
}

int isdigit(char c){
    int i = 0;
    char s[] = "0123456789"
    for (i; i < 10; i++){
        if (c == s[i])
            return 1;
    }
    return 0;
}

int isalnum(char c){
    return isalpha(c) || isdigit(c);
}

*/

