#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <math.h>




int sequence(char [], int);
//int get_move(char);
int next_state(int, char);

int main(void) {
    char seq[10];
    int n;
    scanf("%s %d", seq, &n);
	printf("%d\n", sequence(seq,n));
}

int sequence(char arr[], int n){
    int i, valid, curr_state = 0;

    for (i = 0; i < n; i++){
        valid = next_state(curr_state, arr[i]);
        if (valid)
            curr_state = valid;
        else
            return 0;
    }
    return curr_state == 2;
}

// returns next_state if valid, 0 if invalid
int next_state(int state, char move){
    char arr[] = "acgt";

    //only state 0 has more than 1 valid move
    if (state == 0 && move == 'g')
        return 2;
    else if (arr[state] == move)
        //next state will be state + 1 for states 0-2, but just 2 for state 3
        return state > 2 ? 2: (state + 1);

    //will go here if move is invalid
    return 0;
}


