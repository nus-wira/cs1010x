/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 17, Question 1 Template     *
 *****************************************/

#include <stdio.h>

#define MAX_LEN 80

void fill(char matrix[MAX_LEN][MAX_LEN], char c) {
    int row, col;
    for (row = 0; row < MAX_LEN; ++row) {
        for (col = 0; col < MAX_LEN; ++col) {
            matrix[row][col] = c;
        }
    }
}

void print(char matrix[MAX_LEN][MAX_LEN], int length) {
    int row, col;
    for (col = 0; col < length + 2; ++col) {
        printf("-");
    }
    printf("\n");
    for (row = 0; row < length; ++row) {
        printf("|");
        for (col = 0; col < length; ++col) {
            printf("%c", matrix[row][col]);
        }
        printf("|\n");
    }
    for (col = 0; col < length + 2; ++col) {
        printf("-");
    }
    printf("\n");
}

void spiral(char matrix[MAX_LEN][MAX_LEN], int length, char *text) {
    /************
     *  Task 1  *
     ************

     Parameters:
        matrix - 2D character matrix to fill.
        length - Length of the square matrix to fill. Only row 0 up to
                 row (length - 1) and column 0 up to column (length - 1)
                 will be processed. Take reference from the 'print' function.
                 Length will always be an even +ve number and at most MAX_LEN.
        text   - String to fill the matrix with.

     You are to fill the matrix with characters from the given text in a
     clockwise sequence, starting from the top-left corner, spiraling inwards
     to the center of the matrix. Note that the size of the matrix is limited
     to the given length (MAX_LEN is only for allocating sufficient memory).

     The text string should be used repeatedly if there are not enough
     characters in the text to fill the entire matrix, i.e.
     strlen(text) < length * length. See below for the expected output.
    */
    int count = length*length;
    int side = length;
    int all_i = 0, x = 0, y = 0; //overall index, row index, col index
    int text_i = 0, text_len = 0; // text index and length
    int dir = 0; //direction: 0 right, 1 down, 2 left, 3 right
    //to find text_len
    while (text[text_len] != '\0')
        text_len++;

    while (all_i < count){
        //reset text index if finish
        if (text_i == text_len)
            text_i = 0;

        //if reaching the edges do appropriate adjustment
        if (dir == 0 && y == side){ //right
            y--;
            x++;
            dir = 1;
        }
        else if (dir == 1 && x == side){ //down
            x--;
            y--;
            dir = 2;
        }
        else if (dir == 2 && y == length - side -1){ //left
            y++;
            x--;
            dir = 3;
            side--;
        }
        else if (dir == 3 && x == length - side -1){ //right
            x++;
            y++;
            dir = 0;
        }

        //set the char
        matrix[x][y] = text[text_i++];

        //next tile
        switch(dir){
            case 0:
                y++;
                break;
            case 1:
                x++;
                break;
            case 2:
                y--;
                break;
            case 3:
                x--;
                break;
        }
        all_i++;
    }
}

int main(void) {
    char matrix[MAX_LEN][MAX_LEN] = {{'a'}};
    fill(matrix, ' ');
    spiral(matrix, 10, ".... . ._.. .__. __ .");
    print(matrix, 10);

    spiral(matrix, 20, "\\/");
    spiral(matrix, 14, "TheQuickBrownFoxJumpsOverTheLazyDog");
    print(matrix, 21);
    return 0;
}

/*
 EXPECTED OUTPUT:

    ------------
    |.... . ._.|
    |_. __ ....|
    |_.... . . |
    |..........|
    |    ._ _ _|
    |.__.._..._|
    |.__._. . .|
    |_  .__. . |
    |..__. ..__|
    | . ..... _|
    ------------
    -----------------------
    |TheQuickBrownF\/\/\/ |
    |JumpsOverTheLo/\/\/\ |
    |xTheLazyDogTax\/\/\/ |
    |orheLazyDoghzJ/\/\/\ |
    |FeTpsOverTTeyu\/\/\/ |
    |nvrmuickBhhQDm/\/\/\ |
    |wOeuQJumreeuop\/\/\/ |
    |osvJexspoLQigs/\/\/\ |
    |rpOxhoFnwaucTO\/\/\/ |
    |BmsoTgoDyzikhv/\/\/\ |
    |kupFnworBkcBee\/\/\/ |
    |cJmuJxoFnworQr/\/\/\ |
    |ixoFnworBkciuT\/\/\/ |
    |uQehTgoDyzaLeh/\/\/\ |
    |\/\/\/\/\/\/\/\/\/\/ |
    |/\/\/\/\/\/\/\/\/\/\ |
    |\/\/\/\/\/\/\/\/\/\/ |
    |/\/\/\/\/\/\/\/\/\/\ |
    |\/\/\/\/\/\/\/\/\/\/ |
    |/\/\/\/\/\/\/\/\/\/\ |
    |                     |
    -----------------------
*/
